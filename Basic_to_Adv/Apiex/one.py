# import requests
# import json
# res=requests.get("https://dummyjson.com/products/search?q=Laptop")
# users=res.json()

# fp=open("user.json","w")
# json.dump(fp,users)
# fp.close()
    
import requests 
import json
response=requests.get('https://dummyjson.com/products/1')
product_data=response.json()
# print(type(product_data))
# print(product_data)
for product_datas in product_data.items():
    print(product_datas)

