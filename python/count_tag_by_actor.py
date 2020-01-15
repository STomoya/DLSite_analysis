'''
create json file of:
    {
        <actor-name> : [
            <tags-count>,
            ...
        ],
        ...
    }

for speed:
first make
    {
        <actor-name> : {
            <tag> : <tag-count>,
            ...
        },
        ...
    }
use appeared words as index for dictionary and add 1.
then convert to required shape.
'''

from pathlib import Path
import json

try:
    with open('/src/organized/basic_info.json', 'r', encoding='utf-8') as fin:
        info = json.load(fin)
except Exception as e:
    print(e)
    raise

actors = info['actors']
tags = info['tags']

# initualize actor_tag
actor_tag = {}
for actor in actors:
    actor_tag[actor] = {}
    for tag in tags:
        actor_tag[actor][tag] = 0

# look at each file and count given tags to actors by works
base = Path('/src/data')
paths = base.glob('*.json')
works = [str(path) for path in paths]
for work in works:
    try:
        with open(work, 'r', encoding='utf-8') as fin:
            work_info = json.load(fin)
    except Exception as e:
        print(e)
        raise
    if work_info['actor'] == []:
        continue
    else:
        for actor in work_info['actor']:
            for tag in work_info['tags']:
                actor_tag[actor][tag] += 1

# conveert to required shape
for actor in actors:
    actor_tag[actor] = [value for value in actor_tag[actor].values()]

# save
try:
    with open('/src/organized/actor_tag_count.json', 'w', encoding='utf-8') as fout:
        json.dump(actor_tag, fout, ensure_ascii=False, indent=4)
except Exception as e:
    print(e)
    raise
