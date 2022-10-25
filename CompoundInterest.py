#compound interest module
#compound interest final amount=p(1+(r/n))**(nt)
import math
def compound(p,r,n,t):
    r=r/100      #coverting rate from percentage
    a=p*(math.pow((1+r/n),(n*t)))
    ci=a-p

    if a>100000:
        print("rebate on interest=500")
        a=a-500
        print("interest amount=",ci)
        print("final amount due=",a)
    else:
        print("No rebate on interest")
        print("interest amount=",ci)
        print("final amount due=",a)

