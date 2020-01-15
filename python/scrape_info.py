'''
Everything about scraping information
'''

import time
import json
import re

import requests
from bs4 import BeautifulSoup
import lxml
from tqdm import tqdm

from const import *

def main():
    response = requests.get(BASE_URL+'1')
    soup = BeautifulSoup(response.text, 'lxml')
    max_page = get_max_page(soup)
    time.sleep(1)

    for page in tqdm(range(1, max_page+1)):

        response = requests.get(BASE_URL+str(page))
        soup = BeautifulSoup(response.text, 'lxml')
        
        search_result = soup.find(id='search_result_list')
        work_list = search_result.find('table').find_all('tr', recursive=False)

        for work in work_list:
            try:
                work_info = scrape_one(work)
            except Exception as e:
                print(work)
                raise
            save(work_info)

        # time.sleep(2)

def scrape_one(work):
    work_info = {}

    # actor
    # empty list if none
    actors = work.find(class_='author')
    if actors == None:
        actors = []
    else:
        actors = actors.find_all('a')
    work_info['actor'] = [actor.text for actor in actors]

    # category
    work_info['category'] = work.find(class_='work_category').text

    # description
    work_info['description'] = work.find(class_='work_text').text

    # id
    work_info['id'] = work.find(class_='work_name').a['href'].split('/')[-1].split('.')[0]

    # maker
    work_info['maker'] = work.find(class_='maker_name').a.text.strip('\n')

    # name
    work_info['name'] = work.find(class_='work_name').a.text.replace('スマホ専用', '').strip('\n')

    # price
    price = work.find(class_='strike')
    if price == None:
        price = work.find(class_='work_price')
    work_info['price'] = price.text.strip('円').replace(',', '')

    # release
    work_info['release'] = re.findall(r'[0-9]+', work.find(class_='sales_date').text.strip('販売日:\xa0'))

    # tags
    tag_a = work.find(class_='search_tag').find_all('a')
    work_info['tags'] = [a.text for a in tag_a]

    # thumb-nail
    work_info['thumb'] = 'https:' + work.find('img')['src']

    # url
    work_info['url'] = work.find(class_='work_name').a['href']

    return work_info

def save(work_info):
    filename = './data/{}.json'.format(work_info['id'])
    try:
        with open(filename, 'w', encoding='utf-8') as fout:
            json.dump(work_info, fout, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)
        raise

def get_max_page(soup):
    total_page_element = soup.find(class_='page_total').text
    total_page_element_list = re.findall(r'[0-9]+', total_page_element)
    max_page = int(total_page_element_list[0]) / int(total_page_element_list[2])
    if not int(total_page_element_list[0]) % int(total_page_element_list[2]) == 0:
        max_page += 1
    return int(max_page)

if __name__=='__main__':
    main()
