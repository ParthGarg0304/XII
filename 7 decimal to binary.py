def bin(d):
    if d>=1:
        bin(d//2)
    print(d%2,end='')
    


dec=int(input("enter a decimal number"))
bin(dec)
