import sys
import json
import os

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    except TypeError as err:
        return False
    return True

def build_json(json_items):
    obj = {}
    for item in json_items:
        if os.path.isfile(item):
            with open(item, 'r') as file:
                data = file.read().replace('\n', '')
                obj = {**obj, **json.loads(data)}
        else:
            prepared_item = item.split("=") # an array of [key, value]
            if validateJSON(prepared_item[1]): # if the value is json
                prepared_item = [prepared_item[0], json.loads(prepared_item[1])]
# if item.split("=")[1] starts and ends with either " or ', then treat it as a single value
            elif item.split("=")[1].startswith('"') and item.split("=")[1].endswith('"'):
                prepared_item = [item.split("=")[0], item.split("=")[1][1:-1]]
            elif len(item.split("=")[1].split(",")) > 1: # if the value is a comma delimited list
                prepared_item = [item.split("=")[0], item.split("=")[1].split(",")]
            obj = {**obj, **dict([tuple(prepared_item)])}
    return json.dumps(obj)

print(build_json(sys.argv[1:]))
