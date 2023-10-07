import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["FDetails"]
col=db["Customers"]
col.insert_many([{"id":1,"name":"Ugo"},
{"id":2,"name":"Monte"},
{"id":3,"name":"Dalenna"},
{"id":4,"name":"Giulio"},
{"id":5,"name":"Mandi"},
{"id":6,"name":"Hewie"},
{"id":7,"name":"Larisa"},
{"id":8,"name":"Huntley"},
{"id":9,"name":"Tallie"},
{"id":10,"name":"Chere"}])