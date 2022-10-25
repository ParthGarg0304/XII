#count the number of characters in a string using dictionary

string=input("enter a string")
dict1={}

for i in string:
    count=0
    if i not in dict1:
        count+=1
        dict1[i]=count
    else:
        dict1[i]+=1

for keys in dict1:
    print(keys,':',dict1[keys])
