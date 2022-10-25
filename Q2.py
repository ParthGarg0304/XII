import mysql.connector as mc

sql=mc.connect(host="localhost",user="root",passwd="1234",database="ABCCorps")
if not sql.is_connected():
    print("Not Connected successfully")

dbcursor=sql.cursor() #database cursor
#execute the command in mysql
dbcursor.execute("create table Employee(Emp_No char(4) primary key, Emp_Name varchar(15),Gender char(1), Salary int,DOJ date)")
dbcursor.execute("insert into Employee values('1','Mukesh Gupta','M',50000,'1998-04-21')")
dbcursor.execute("insert into Employee values('2','Kanika Singh','F',100000,'2000-12-02')")
dbcursor.execute("insert into Employee values('3','Raj Kapoor','M',48000,'1999-08-11')")
dbcursor.execute("insert into Employee values('4','Pankaj Kumar','M',750000,'1989-04-01')")
dbcursor.execute("insert into Employee values('5','Khushi Gupta','F',80000,'1993-09-03')")

year=int(input("enter year in the form yyyy"))
dbcursor.execute("select * from Employee where Gender='F' and DOJ like 'year%'")
data=dbcursor.fetchall() #fetch all the data from that command
for i in data:
    print(i)
    
dbcursor.execute("select Gender,max(Salary),min(Salary) from Employee group by Gender")
data=dbcursor.fetchall()
for i in data:
    print(i) #each record as a tuple in a new line


sql.close()
