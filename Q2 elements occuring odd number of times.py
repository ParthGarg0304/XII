#elements occuring odd number of times

l=eval(input("enter a list"))
odd=[]     #list containing elements occuring odd number of times
for i in l:
    c=0
    for j in range(len(l)):
        if l[j]==i:
            c+=1
    if c%2==1:
        if i not in odd:
            odd+=i

for i in odd:
    print(i)

#can also use count function
