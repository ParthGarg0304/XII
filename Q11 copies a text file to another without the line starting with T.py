"""Write a program that copies a text file “source.txt” onto “target.txt” barring
the lines starting with a ‘T’."""

f=open("source.txt","r")
with open ("target.txt","w+") as f2:
    for line in f:
        if line[0]!="T":
            f2.write(line)
            print(line)

f.close()
f2.close()

