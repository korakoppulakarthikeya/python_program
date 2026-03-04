import json
data={
    'student':[
        {'name': 'karthikeya','age':23,"gender":"M"},
        {"name":"harish","age":24,"gender":"M"}
    ]
}
with open("file.json","w") as f :
    json.dump(data,f,indent=4)

    