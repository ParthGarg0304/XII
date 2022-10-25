def convert(n):
    word=''
    while n!=0:
        d=n%10
        if d==1:
            word='One '+word
        elif d==2:
            word='Two '+word
        elif d==3:
            word='Three '+word
        elif d==4:
            word='Four '+word
        elif d==5:
            word='Five '+word
        elif d==6:
            word='Six '+word
        elif d==7:
            word='Seven '+word
        elif d==8:
            word='Eight '+word
        elif d==9:
            word='Nine '+word
        else:
            word='Zero '+word
        n=n//10
    return word
        
num=int(input("enter a number"))
print("number converted to word::",convert(num))
