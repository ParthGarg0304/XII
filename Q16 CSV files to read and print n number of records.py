"""Create a CSV file with n no. of records and structure of each record is in the format
[id, destination, days, fare]. N is provided by the user. Write another function that
will read and print the records in the file."""

import csv

def readprint():
    f=open("file.csv","r")
    read=csv.reader(f)
    for line in read:
        print(line)
    f.close()
    

n=int(input("enter the number of records"))
f=open("file.csv","w",newline='')
writer=csv.writer(f)
l=[['id','destination','days','fare']]
writer.writerow(l)

for i in range(n):
    record=[]
    id=int(input("enter the id"))
    record.append(id)
    dest=input("enter the destination")
    record.append(dest)
    day=int(input("enter the number of days"))
    record.append(day)
    fare=int(input("enter the fare"))
    record.append(fare)
    l.append(record)
writer.writerows(l)
f.close()

readprint()


