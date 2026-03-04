import json
with open("/Users/codegnan/file/file3.json",'r')as f:
    data = json.load(f)
    print(data)
    for i in data:

        print(i['name'])