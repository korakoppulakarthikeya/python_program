import json
with open("/Users/codegnan/file/file3.json",'r')as f:
    data = json.load(f)
    data.append({"name":"harish","age":23})
with open ("/Users/codegnan/file/file3.json",'w') as f:
    json.dump(data,f,indent=4)
