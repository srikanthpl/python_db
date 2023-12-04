import requests
import mysql.connector

api_url="https://jsonplaceholder.typicode.com/todos/10"
response=requests.get(api_url)

if response.status_code==200:
    api_data=response.json()
else:
    print("Error")


db_connection = mysql.connector.connect(host="localhost",user="root",password="Sri@1234",database="api")

cursor=db_connection.cursor()

for item in api_data:
    query="INSERT INTO "
