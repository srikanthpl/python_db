import re
mobilenumber=input("Enter The Number:")
validation=re.fullmatch("[6-9]\d{9}",mobilenumber)
if validation:
    print("Valid Number")
else:
    print("Not Valid")