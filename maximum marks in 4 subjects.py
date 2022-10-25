d={}
for i in range(4):
    key=input('enter subject')
    val=int(input('enter marks scored in corrsponding subject'))
    d[key]=val
    
maximum=0
maxi=''
for i in d:
    if d[i]>maximum:
        maxi=i

print('highest marks scored in',maxi,'=',d[maxi])

