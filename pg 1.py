def PUSH(employee):
    ch="y"
    while ch=="y":
        n=input("enter employee name")
        employee.append(n)
        ch=input("do you want to enter more employees(y/n)")
    display(employee)


def display(employee):
    print(employee[::-1])
    

employee=[]
PUSH(employee)
