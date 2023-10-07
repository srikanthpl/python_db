import re
num="mobile no: 8838778863876"
found=re.sub("[2-9]","*",num)
print(found)