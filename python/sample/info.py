'''
Checking format of the web page.
'''

import pprint
import re

import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.dlsite.com/maniax/fsr/=/language/jp/sex_category%5B0%5D/male/ana_flg/off/work_category%5B0%5D/doujin/order%5B0%5D/release_d/genre_and_or/or/options_and_or/or/per_page/100/show_type/1/page/1'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

search_result = soup.find(id='search_result_list')
work_list = search_result.find('table').find_all('tr', recursive=False)

for work0 in work_list:

    work_info = {}

    work_info['category'] = work0.find(class_='work_category').text

    work_info['name'] = work0.find(class_='work_name').a.text.strip('\n')

    work_info['maker'] = work0.find(class_='maker_name').a.text.strip('\n')

    price = work0.find(class_='strike')
    if price == None:
        price = work0.find(class_='work_price')
    work_info['price'] = price.text.strip('円').replace(',', '')

    actors = work0.find(class_='author')
    if actors == None:
        actors = []
    else:
        actors = actors.find_all('a')
    work_info['actor'] = [actor.text for actor in actors]

    work_info['description'] = work0.find(class_='work_text').text

    tag_a = work0.find(class_='search_tag').find_all('a')
    work_info['tags'] = [a.text for a in tag_a]

    work_info['release'] = re.findall(r'[0-9]+' ,work0.find(class_='sales_date').text.strip('販売日:\xa0'))

    work_info['url'] = work0.find(class_='work_name').a['href']

    work_info['id'] = work_info['url'].split('/')[-1].split('.')[0]

    work_info['thumb'] = 'https:' + work0.find('img')['src']

    pprint.pprint(work_info)

    break
