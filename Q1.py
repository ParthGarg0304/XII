#NOP number of participants
import mysql.connector as mc

sql=mc.connect(host="localhost",user="root",passwd="1234",database="Programme")
if not sql.is_connected():
    print("Not Connected successfully")

dbcursor=sql.cursor() #database cursor
#execute the command in mysql
dbcursor.execute("create table Event(E_No char(4) primary key, E_Name varchar(15), NOP int,E_Date date)")
dbcursor.execute("insert into Event values('1','Wedding',100,'2022-04-21');")
dbcursor.execute("insert into Event values('2','Birthday',20,'2022-05-10');")
dbcursor.execute("insert into Event values('3','Party',15,'2022-11-29');")
dbcursor.execute("insert into Event values('4','Funeral',7,'2022-04-01');")
dbcursor.execute("insert into Event values('5','Farewell',75,'2022-09-03');")
print("records where NOP is more than 10.")
dbcursor.execute("select * from Event where NOP>10")
data=dbcursor.fetchall() #fetch al the data from that command
for i in data:
    print(i) #each record as a tuple in a new line
    
print("")

print("the table contents in ascending order of E_Date.")
dbcursor.execute("select * from Event order by E_Date asc")
data=dbcursor.fetchall() #fetch al the data from that command
for i in data:
    print(i) #each record as a tuple in a new line

sql.close()
