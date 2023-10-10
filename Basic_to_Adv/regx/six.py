import re
plate=input("Enter the Plate No:")#TN70AH5974
val=re.fullmatch("TN[701]{2}[A-Z]{2}\d{4}",plate)
if val:
    print("Valid")
else:
    print("Not Valid")