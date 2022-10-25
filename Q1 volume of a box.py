#volume of a box

def vol(l=5,w=5,h=5):
    volume=l*w*h
    return volume
l=int(input("enter the length of the box"))
w=int(input("enter the width of the box"))
h=int(input("enter the height of the box"))
print("volume of the box is::",vol(l,w,h))
