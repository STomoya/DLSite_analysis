from pathlib import Path
import json

base = Path('/src/data')
paths = base.glob('*.json')
works = [str(path) for path in paths]

tags = set()
actors = set()
category = set()
for work in works:
    try:
        with open(work, 'r', encoding='utf-8') as fin:
            data = json.load(fin)
        tags |= set(data['tags'])
        actors |= set(data['actor'])
        category.add(data['category'])
    except Exception as e:
        print(e)

info = {
    'tags' : list(tags),
    'actors' : list(actors),
    'category' : list(category)
}
try:
    with open('/src/organized/basic_info.json', 'w', encoding='utf-8') as fout:
        json.dump(info, fout, ensure_ascii=False, indent=4)
except Exception as e:
    print(e)