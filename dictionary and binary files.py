"""WAP to create a dictionary to accept the record of 10 students having the following keys : S_ID, S_Name, Event
and store the records in an binary file "Sports.dat".
The events available : "flat race", "hurdle race",
"javline throw", "archery" and "fencing". Due to lack of equipment, the 
institution decided to cancel the "hurdle race" event and it was decided 
that all those participants will participate in "flat race" instead. 
WAP to update the file as per the latest changes.  """

import pickle

def check():
    print("hurdle race event is canceled")
    try:
        while True:
            l=pickle.load(f)
            if l["Event"]=="hurdle race":
                l["Event"]="flat race"
                print(l)
            else:
                print(l)
    except EOFError:
        print("end of file")
        f.close()
            

print("event list:flat race,hurdle race,javline throw, archery and fencing")
f=open("record.dat","wb+")
for i in range(0,10):
    d={}
    id_no=int(input("enter the student id"))
    name=input("enter the student name")
    event=input("enter the event the student wants to take part in")
    d["S_ID"]=id_no
    d["S_Name"]=name
    d["Event"]=event
    print("student record:",d)
    pickle.dump(d,f)

f.seek(0)
check()    
    
