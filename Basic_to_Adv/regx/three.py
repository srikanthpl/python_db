import re
data="helloGuys"
found=re.subn("[a-z | A-Z]",">",data)
print(found)