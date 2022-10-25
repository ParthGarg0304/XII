"""Write a python function that reads the above CSV file and prints the records where
the destination takes less than 15 days. The function accepts the name of the file as
argument."""

import csv

def check(read):
    print("records where the destination takes less than 15 days")
    for line in read:
        print(line)
    f.close()
    

n=int(input("enter the number of records"))
f=open("file.csv","w",newline='')
writer=csv.writer(f)
l=[['id','destination','days','fare']]

for i in range(n):
    record=[]
    id=int(input("enter the id"))
    dest=input("enter the destination") 
    fare=int(input("enter the fare"))
    day=int(input("enter the number of days"))
    if day>15:
        print("invalid day equirements")
        print("enter new record")
        continue
    record.append(id)
    record.append(dest)
    record.append(day)
    record.append(fare)
    l.append(record)
    p=(id,dest,day,fare)
writer.writerows(p)
f.close()

f=open("file.csv","r")
read=csv.reader(f)

check(read)
