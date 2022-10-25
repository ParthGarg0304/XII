#hcf of two numbers using recursion
def hcf(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return hcf(a-b,b)
    return hcf(a,b-a)
    
x=int(input("enter a number"))
y=int(input("enter a number"))
print("the H.C.F is::",hcf(x,y))
