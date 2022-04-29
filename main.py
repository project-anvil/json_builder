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
            prepared_item = item.split("=") if len(item.split("=")[1].split(",")) == 1 else [item.split("=")[0], item.split("=")[1].split(",")]
            obj = {**obj, **dict([tuple(prepared_item)])}
    return json.dumps(obj)

print(build_json(sys.argv[1:]))