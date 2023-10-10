import re
val=input("Enter The Input:")#Sri1211@gmail.com
result=re.fullmatch("\w{7}\W[a-z]{5}.\w{3}",val)
if result:
    print("valid")
else:
    print("Not valid")