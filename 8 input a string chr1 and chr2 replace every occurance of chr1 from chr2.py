#input a string chr1 and chr2 replace every occurance of chr1 from chr2

def repcl(string,a,b):
    word=''
    for i in string:
        if i==a:
            word=word+b
        else:
            word=word+i
    return word
    
string=input("enter a sentence")
x=input('enter the character that is to be replaced')
y=input('enter the character that is to be replaced with')
print("string after replacing the characters",repcl(string,x,y))
