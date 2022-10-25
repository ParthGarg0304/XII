def pushstack(d,l):
    pushlist=[]
    for i in l:
        if d[i]>75:
            pushlist.append(i)
    return pushlist

def delete(pl):
    pl.pop()
    return pl
    
def display(pl):
    print(pl[::-1])

    
d={}
l=[]
for i in range(0,6):
    name=input("enter student name")
    l.append(name)
    marks=int(input("enter student marks"))
    d[name]=marks

print("1:add name of the student with more than 75 marks")
print("2:delete a name from the name list")
print("3:display the record")
choice="y"
while choice=="y":
    ch=int(input("enter your choice"))
    if ch==1:
        pl=pushstack(d,l)
    elif ch==2:
        pl=delete(pl)
    elif ch==3:
        display(pl)
    else:
        print("wrong choice")
    choice=input("do you want to continue with choices(y/n)")


