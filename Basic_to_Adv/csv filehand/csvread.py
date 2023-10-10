import csv
f=open("one.csv","r")
cp=csv.reader(f)
print(cp)
print(type(cp))
print(list(cp))