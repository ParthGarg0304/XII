#two tuples,remove the elements from tuple2 which are present in tuple1\
t1=eval(input("enter a tuple"))
t2=eval(input("enter a tuple"))
t2new=tuple() #new tuple2 after editing
print('2nd tuple before editing::')
print(t2)

for i in t1:
    k=0
    for j in t2:
        if j==i:
            k+=1
    temp=(i)
    if k==0:
        t2new=t2new+temp

print("1st tuple::")
print(t1)
print("2nd tuple::")
print(t2new)

#temp=tuple()
