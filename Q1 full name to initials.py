#full name to initials
n=input("enter your full name")
n=n.title()
n=n+' '
x=''
new=''
l=list()
l=n.split()

for i in range(len(l)-1):
    x=l[i]
    new+=x[0]+'.'
new+=l[len(l)-1]
 

print(new)
