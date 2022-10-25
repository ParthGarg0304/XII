#DDMMYYYY
n=input("enter the date in the for of DDMMYYYY")
d=n[0:2]
m=int(n[2:4])
y=int(n[4:])
suffix=''
mname=''
if d==1:
    suffix='st'
elif d==2:
    suffix='nd'
elif d==3:
    suffix='rd'
else:
    suffix='th'
name=['january','feburary','march','april','may','june','july','august','september','october','november','december']
mname=name[m-1]
dth=d+suffix
print(dth,mname,end=',')
print(y)
