#prime number or not
def prime(n):
    k=0
    for i in range(1,n+1):
        if n%i==0:
            k+=1
    if k==2:
        return True
    else:
        return False

num=int(input("enter a number"))
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
