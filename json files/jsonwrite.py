import json
f=open("two.json","w")
emp_dict={
    'id':101,
    'name':'sri',
    'avail':True }
json.dump(emp_dict,f)
