#frequency of substring
n=input("enter a sentence")
sub=input("enter the part of the string to be searched for frequency")
ctr=0
n=n+" "
x=""
for i in n:
    if i!=" ":
        x=x+i
    else:
        length=len(sub)
        for i in range(len(x)):
            if x[i:i+length]==sub:
                ctr+=1
        x=""

print(sub,"occured",ctr,"times")

