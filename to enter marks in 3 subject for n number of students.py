#to enter marks in 3 subject for n number of students

import pickle
l=[]
marks=[]
f=open("marks.dat","wb+")
n=int(input("ente the number of records"))

for i in range(n):
    roll=int(input("enter the roll number::"))
    l.append(roll)
    name=input("enter the name::")
    l.append(name)
    for j in range(3):
        x=float(input("enter the marks::"))
        marks.append(x)
    l.append(marks)
    pickle.dump(l,f)
    l=[]
    marks=[]

f.seek(0)
try:
    while True:
        l=pickle.load(f)
        print(l)

except EOFError:
    print("end of file")
    f.close()
    
    
