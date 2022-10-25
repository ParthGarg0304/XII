#using multiple functions
def prime(n):
    f=0
    for i in range(1,n+1):
        if(n%i==0):
            f+=1
    if(f==2):
        palin(n)
    else:
        print(n,"is a not  prime palindrome number")


def palin(n):
    num=n
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if(num==rev):
        print(num,"is a prime palindrome number")
    else:
        print(num,"is not a prime palindrome number")


x=int(input("enter a number"))
prime(x)
