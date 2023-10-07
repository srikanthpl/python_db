import re 
pwd = input("Enter Password:")
result = re.fullmatch("[^a-zA-Z0-9]{1}+\w{5,8}", pwd)
if result:
    print("Valid")
else:
    print("Not Valid")