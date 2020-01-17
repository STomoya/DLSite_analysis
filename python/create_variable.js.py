
import json
import numpy as np

try:
    with open('/src/organized/basic_info.json', 'r', encoding='utf-8') as fin:
        basic_info = json.load(fin)
except Exception as e:
    print(e)
    raise

js_str = 'var basic_data = {\n'

# tags
sorted_tags = np.argsort(basic_info['tags'])

js_str += '    \"labels\":['
for index in sorted_tags:
    line = '\"{}\",'.format(basic_info['tags'][index])
    js_str += line
js_str += '],\n'

# colors
js_str += '    \"colors\":['
for index, _ in enumerate(sorted_tags):
    colors = ['#0088ff', '#88ff00', '#ff0088', '#0000ff', '#00ff00', '#ff0000']
    line = '\"{}\",'.format(colors[index%len(colors)])
    js_str += line
js_str += '],\n'

# actors
sorted_actors = sorted(basic_info['actors'])

js_str += '    \"actors\":['
for actor in sorted_actors:
    line = '\"{}\",'.format(actor)
    js_str += line
js_str += ']\n'

js_str += '}\n'

del basic_info

# { <actor> : <list of tag counts> }
js_str += '\n'
try:
    with open('/src/organized/actor_tag_count.json', 'r', encoding='utf-8') as fin:
        actor_tag = json.load(fin)
except Exception as e:
    print(e)
    raise

js_str += 'var full_data = {\n'
for actor in sorted_actors:
    js_str += '    "{}":['.format(actor)
    for index in sorted_tags:
        js_str += ' {},'.format(actor_tag[actor][index])
    js_str += '],\n'
js_str += '}\n'

try:
    with open('/src/js/variable.js', 'w') as fout:
        fout.write(js_str)
except Exception as e:
    print(e)
    raise