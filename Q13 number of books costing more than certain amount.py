"""Write a function counting() that accepts an argument price. The function should
print the total number of books that cost more than the value of the argument
passed. Use the file Book.dat created in the previous program."""

import pickle

def Counting(price):
    try:
        while True:
            list=pickle.load(f)
            print(list)
            if list[3]>price:
                c=c+1
    except EOFError:
        print("end of program")
        f.close()
    return c


l=[]
f=open("Book.dat","wb+")
n=int(input("enter the number of records"))
for i in range(n):
        bno=int(input("enter the book number::"))
        l.append(bno)
        bname=input("enter the book name::")
        l.append(bname)
        author=input("enter the Author name::")
        l.append(author)
        price=float(input("enter the price::"))
        l.append(price)
        pickle.dump(l,f)
        l=[]
f.seek(0)

p=int(input("enter the price of the book"))
c=Counting(p)
print("number of books that cost more than",p,"is",c)
