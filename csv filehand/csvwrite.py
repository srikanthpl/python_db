import csv
f=open("one.csv","w",newline="\n")
cp=csv.writer(f)
cp.writerow(["id","Name","Sal"])
cp.writerow([101,"rahul",10000])
print(cp)

# iterating the writer method
for i in range(5):
    id=input("Enter the Id:")
    name=input("Enter the Name:")
    sal=input("Enter the Salary:")
    print(id,name,sal)
f.close()