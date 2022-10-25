#linear search
l1=eval(input("enter a list of numbers"))
ns=int(input("enter the nmber to be searched"))
k=0
for i in l1:
    if i==ns:
        print('search successful')
        k=1
        break

if k==0:
    print("search unsuccessful")
