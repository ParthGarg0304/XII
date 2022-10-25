#minimum ones digit

def onesDigit(a,b):
    if(a%10)<(b%10):
        return a
    else:
        return b

x=int(input("enter a number"))
y=int(input("enter a number"))
print("the number with minimum ones digit is::",onesDigit(x,y))
