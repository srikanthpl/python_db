arr=[1,3,5,7,9]
data=[]
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        if j==i:
            continue
        sum=sum+arr[j]
    data.append(sum)
l=0
s=10000
for i in  range(len(data)):
    if l<=data[i]:
        l=data[i]
    if s>=data[i]:
        s=data[i]
print(s,l)