n=int(input("enter the number of terms"))
d={}
for i in range(n):
    key=input('enter the key')
    val=input('enter value for the corrsponding key')
    d[key]=val
l=[]
l2=[]
for keys in d:
    if d[keys] not in l:
        l.append(d[keys])
    else:
        l2.append(d[keys])

for j in l:
    if j not in l2:
        print(j)
