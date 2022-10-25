"""Write a program in Python that counts total number of “the” word present in
a text file named “nice.txt”."""

#A Text file nice.txt was created explicitly

with open("nice.txt","r")as f:
    c=0
    for line in f:
        words =line.split()
        for i in words:
            if i=="the" or i=="The":
                c+=1

print("number of 'The' is the text file is",c)
f.close()

