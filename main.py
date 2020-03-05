import sys
import json
import os

def build_json(json_items):
    obj = {}
    for item in json_items:
        if os.path.isfile(item):
            with open(item, 'r') as file:
                data = file.read().replace('\n', '')
                obj = {**obj, **json.loads(data)}
        else:
            obj = {**obj, **dict([tuple(item.split("="))])}
    return json.dumps(obj)

print(build_json(sys.argv[1:]))