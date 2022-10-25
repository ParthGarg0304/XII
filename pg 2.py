#WA menu driven program

def add(l):
    ch="y"
    while ch=="y":
        record=eval(input("enter a book record id,type,cost"))
        l.append(record)
        ch=input("do you want to continue entering more records(y/n)")
    return l

def peek(l):
    print(l[-1])
     
def delete(l):
    l.pop()
    return l

def display(l):
    print(l[::-1])

l=[]
print("1:add a record")
print("2:peek the record")
print("3:delete a record")
print("4:display the records")
choice="y"
while choice=="y":
    ch=int(input("enter your choice"))
    if ch==1:
        l=add(l)
    elif ch==2:
        peek(l)
    elif ch==3:
        l=delete(l)
    elif ch==4:
        display(l)
    else:
        print("wrong choice")
    choice=input("do you want to continue with choices(y/n)")

