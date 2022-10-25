#a program to creat a dictionary from a string where keys are the words and values are the frequency of the word in the string.input is a sentence from the user
n=input("enter a sentence")
l=list()
l=n.split()
d={}
for i in l:
    freq=0
    for j in range(len(l)):
        if l[j]==i:
            freq+=1
    d[i]=freq
    
        
print(d)
