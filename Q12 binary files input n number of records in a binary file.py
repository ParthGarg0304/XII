"""Write a function CreateFile() to input n number of records in a binary file
'Book.Dat' with a structure [BookNo, BookName, Author, Price], where n is given by
the user."""

import pickle

def CreateFile(n,l):
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
    print("[Book Number,Book Name,Author,Price]")
    try:
        while True:
            l=pickle.load(f)
            print(l)

    except EOFError:
        print("end of file")
        f.close()


    
    
l=[]
f=open("Book.dat","wb+")
n=int(input("enter the number of records"))
CreateFile(n,l)
