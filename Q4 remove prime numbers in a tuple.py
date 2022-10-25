#remove prime numbers from a tuple
t=eval(input("enter a numerical tuple"))
k=0
l=[]
for i in t:
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k+=1

    if k!=2:
        l.append(i)
print(l)

