def ch(x,y):
    temp=""
    c=0
    for i in x:
        if i==y:
            c+=1
        else:
            temp+=i

    if c==0:
        print("substring not found")
    return(temp)

print(ch('hello my name is parth','l'))
