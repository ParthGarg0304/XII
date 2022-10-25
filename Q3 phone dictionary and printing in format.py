d={}
for i in range(10):
    name=input('enter your friend name')
    num=int(input('enter the phone number for corrsponding name'))
    d[name]=num

for keys in d:
    print(keys,":",d[keys])
    
