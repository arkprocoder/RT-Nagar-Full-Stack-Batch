# import math
# print(math.pi)
# def add(a,b):
#     sum=a+b
#     print('sum is ',sum)

# def mul(a,b,c):
#     res=a*b*c
#     print('mul is ',res)

# add(5,10)
# mul(3,3,3)


import math

def circle(r):
    result=r*r*math.pi
    return result
    
print("area of the circle")
r=int(input("enter the raidus:\n"))
aoc=circle(r)
print("area of the circle",aoc)

def rectangle(l,b):
    result=l*b
    print("area of the rect",result)
    # return result

def square(a):
    res=a*a
    return res

def triangle(b,h):
    res=0.5*b*h
    return res


print("area of the square")
r=int(input("enter the side:\n"))
aoc=square(r)
print("area of the square",aoc)

print("area of the rectangle")
l=int(input("enter the length:\n"))
b=int(input("enter the breadth:\n"))
rectangle(l,b)
# aoc=rectangle(l,b)
# print("area of the reactangle",aoc)

print("area of the triangle")
l=int(input("enter the base:\n"))
b=int(input("enter the height:\n"))
aoc=triangle(l,b)
print("area of the triangle",aoc)