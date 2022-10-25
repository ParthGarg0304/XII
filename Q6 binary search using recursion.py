#Write a Recursive function in python BinarySearch(Arr,l,R,X) to search the givenelement X to be searched from the List Arr having R elements, where l represents lower bound and R represents the upper bound.

def BinarySearch(Arr,I,R,X):
    if I<=R:
        mid=(I+R)//2
        if X==Arr[mid]:
            return mid
        elif X>Arr[mid]:
            I=mid+1
            return BinarySearch(Arr,I,R,X)
        else:
            R=mid-1
            return BinarySearch(Arr,I,R,X)
    return -1

R=int(input("enter the number of elements"))            
Arr=eval(input("enter a list containing corresponding number of elements"))
X=eval(input("enter the element to be searched"))
pos=BinarySearch(Arr,0,R-1,X)
if pos>=0:
    print('element is present at index',pos)
else:
    print('element is not present in the list')

