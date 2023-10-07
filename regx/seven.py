import re
mail=input("Enter Your Email:")#Sri1211@gmail.com
val=re.fullmatch("\w{5,20}@gmail.com",mail)
if val:
    print("Valid")
else:
    print("Not Valid")