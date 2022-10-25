#removing dublicate

#using count function
l=eval(input("enter a list of words"))

for i in l:
    if l.count(i)!=1:
        while l.count(i)>1:
            index=l.index(i)
            l.remove(i)


print(l)
