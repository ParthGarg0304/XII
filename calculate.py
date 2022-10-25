#calculating module
import math

def square(a):
    area=a*a
    perimeter=4*a
    print("area of square::",area)
    print("perimeter of square::",perimeter)

def rectangle(l,b):
    area=2*(l+b)
    perimeter=l*b
    print("area of rectangle::",area)
    print("perimeter of rectangle::",perimeter)

def triangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    perimeter=a+b+c
    print("area of triangle::",area)
    print("perimeter of triangle::=",perimeter)

def circle(r):
    pi=math.pi
    area=pi*(r*r)
    circumference=pi*2*r
    print("area of circle::",area)
    print("perimeter of circle::",circumference)

def cylinder(r,h):
    pi=math.pi
    surfacearea=(2*pi*r*h)+(2*pi*(r*r))
    print("surface area of cylinder::",surfacearea)

    
