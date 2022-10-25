import CompoundInterest

p=int(input("enter the sum of amount"))
r=int(input("enter the rate of interest in percentage"))
t=int(input("enter the time period in year"))
n=int(input("enter the number of times principal compounded per year"))

CompoundInterest.compound(p,r,n,t)
