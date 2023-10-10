import re
data="Full Stack Developer"
found=re.search("Full",data)
print(found)
print(found.group())
if found:
    print("It founds")
else:
    print("Not Found")