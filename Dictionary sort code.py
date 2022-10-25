#sorting in dictionary is not always true as it is a unordered pair

'''
#input using eval
d=eval(input('enter a dictionary'))
print(d)
'''

#input using loops
n=int(input('enter the number of elements'))
d={}
for i in range(n):
    key=input('enter a key::')
    value=int(input('enter the corrsponding value'))
    d[key]=value
print('the entered dictionary::')
print(d)
l=list(d.keys())
for i in range (len(l)):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

dict1={}
for i in l:
    for key in d:
        if i==key:
            dict1[i]=d[key]

print('sorted dictionary::')
print(dict1)
    
