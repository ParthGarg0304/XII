fruit={}
l=['orange','apple','grapes']
ctr=0
for index in l:
    if index in fruit:
        fruit[index]=ctr
    ctr+=1
print(fruit)
#O/P is empty dictionary
#to make it work
'''
fruit={}
l=['orange','apple','grapes']
ctr=0
for index in l:
    if index not in fruit:
        fruit[index]=ctr
    ctr+=1
print(fruit)
'''
