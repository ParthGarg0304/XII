#binary search without recursion
#ascending order

def binarySearch(l1,key):
    lb=0
    ub=len(l1)-1
    while lb<=ub:
        mid=(lb+ub)//2
        if key==l1[mid]:
            return mid
        elif key<l1[mid]:
            ub=mid-1
        else:
            lb=mid+1
    return -1
            
l=eval(input("enter a list of numbers"))
ns=int(input("enter the nmber to be searched"))
pos=binarySearch(l,ns)
if pos>=0:
    print('search successful')
else:
    print('search unsuccessful')

