"""Write a function Filter_book() that will copy the information about the books by
the given Author from "Book.dat" to another file "Book_new.dat";. After copying delete
Book.dat. The name of the author will be passed as an argument to the function."""


import pickle
import os

def Filter_book(author):
    try:
        while True:
            new=[]
            list1=pickle.load(f)
            if list1[2]==author:
                new.append(list1)
                pickle.dump(new,f2)
                new=[]
                
    except EOFError:
        f.close()
        os.remove("Book.dat")
        print("File deleted")
    call()

def call():
    f2.seek(0)
    try:
        while True:
            list2=pickle.load(f2)
            print(list2)
                
    except EOFError:
        print("end of file")
        f2.close()


l=[]
f=open("Book.dat","wb+")
f2=open("Book_new.dat","wb+")
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
author=input("enter the name of the author")
Filter_book(author)

