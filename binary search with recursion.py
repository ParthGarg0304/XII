#binary search with recursion
#ascending order
def binarySearch(list1,lb,ub,x):
    if lb<=ub:
        mid=(lb+ub)//2
        if x==list1[mid]:
            return mid
        elif x>list1[mid]:
            lb=mid+1
            return binarySearch(list1,lb,ub,x)
        else:
            ub=mid-1
            return binarySearch(list1,lb,ub,x)
    return -1
            
l=eval(input("enter a list of numbers"))
x=int(input("enter the nmber to be searched"))
pos=binarySearch(l,0,len(l)-1,x)
if pos>=0:
    print('element is present at index',pos)
else:
    print('element is not present in the list')
