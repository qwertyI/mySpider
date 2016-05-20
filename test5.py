import json
with open('./detail.json', 'r') as f:
    topic = json.load(f)[0]
    for k in topic:
        print topic[k]