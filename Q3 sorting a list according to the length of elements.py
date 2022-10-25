#sorting a list according to the length of elements

l=eval(input("enter the list elements"))
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if len(l[j])>len(l[j+1]):
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print("the sorted list",l)




