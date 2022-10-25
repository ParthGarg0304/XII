n=int(input("enter the number of employees"))
d={}
for i in range(n):
    key=input('enter the employee name')
    val=int(input('enter salary amount(in rupees) for the corrsponding employee'))
    d[key]=val
    
print(d)
