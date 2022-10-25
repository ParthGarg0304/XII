#a program to creat a dictionary from a string where keys are the words and values are the frequency of the word in the string.input is a sentence from the user
n=input("enter a sentence")
l=list()
l=n.split()
d={}
for i in l:
    count=0
    if i not in d:
        count+=1
        d[i]=count
    else:
        d[i]+=1

for keys in d:
    print(keys,':',d[keys])
    

