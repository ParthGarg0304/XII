#list bubble sort
listl=eval(input("enter the list elements"))
for i in range(len(listl)):
    for j in range(len(listl)-1-i):
        if listl[j]>listl[j+1]:
            temp=listl[j]
            listl[j]=listl[j+1]
            listl[j+1]=temp
print("the sorted list",listl)
