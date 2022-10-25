#very good to splendid
n=input("enter a sentence")
n=n+' '
x=''
new=''
l=list()
l=n.split()

for i in range(len(l)-1):
    if l[i]=='very' and l[i+1]=='good':
        l.pop(i)
        l.pop(i+1)
        l.insert(i,'splendid')

for i in range(len(l)):
    new+=l[i]+' '

        
print(new)

    

    
