"""Write a function named Update_book() that will update the file ​"​Book.dat​";​ created
in the previous program. The function will change​ ​​cost​ only. The new cost of the
book will be given by the user."""

import pickle

def Update_book():
    x=[]
    record=int(input("enter the book number whose price is to be changed"))
    new=int(input("enter the new price for Book::"))
    try:
        while True:
            list1=pickle.load(f)
            x.append(list1)
            print(list1)
    except EOFError:
        print("all old records shown")
        f.close()
    for i in x:
        if i[0]==record:
            i[3]=new
    f1=open("Book.dat","wb+")#it will overwrite the records so previous records are not shown
    for i in x:
        pickle.dump(i,f1)
        f1.seek(0)
        
    try:
        while True:
            list2=pickle.load(f1)
            print(list2)
    except EOFError:
        print("all newrecords shown")
        f.close()
    


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

Update_book()
