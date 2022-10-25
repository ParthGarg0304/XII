#first and last character of every word exchanged

n=input('enter a sentence')
n=n+' '
new=''      #new string


for i in range(len(n)):
    f=''        #first character
    l=''        #last character
    x=''        
    y=''        #new word
    if n[i]!=" ":
        x=x+n[i]
    else:
        f=x[0]
        l=x[len(x)-1]
        y=l+x[1:len(x)-1]+f
    new+=y

print(new)

