import requests
import json
import csv
api_url = "https://jsonplaceholder.typicode.com/todos/10"

#{'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.delete(api_url, json=todo)
data=response.json()
# sri=list(data)
# print(type(sri))
# for i in sri:
#     print(i)
file=open("user2.json","w")
json.dump(data,file)
file.close()

#  {"userId": 1, "title": "Wash car", "completed": True}
