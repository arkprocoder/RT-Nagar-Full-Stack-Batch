'''
1) write a program to take a input from the user and print the details
   *Employee Name
   *Employee Age
   *Employee Phone Number\
   *EMployee Address
along with this print the type of all the variables


'''
'''
name=input("enter name :\n")
age=input("enter age :\n")
number=input("enter number :\n")
address=input("enter address :\n")
age=int(age)
number=int(number)
print(name,age,number,address)
print(type(name),type(age),type(number),type(address))
'''

'''
2)write a program to take a input from the user and print the details
  *Student Name 
  *Student maths marks
  *Student science marks

->print student name in Upper case
->add students marks (math+science) then print the total marks
->then find the average of two subjects

'''

'''
name=input("enter student name :\n")
maths=input("enter maths mark :\n")
science=input("enter science mark :\n")

total=int(maths)+int(science)
print(total)
print(f'average is {total/2}')

'''
'''
3)mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
mystr= "Quick Step Bangalore"
1)write a python program to evaluate below list
a)Add the items in list 
b)Find the length of the list
c)sort the elements from the list
d)reverse the list
e)Count the duplicates elements from the list (3,2)
g)print "Step" using slicing
h)print "Bangalore" using negative index
i)print "QB"
'''
'''
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
mylist.append(150)
print(len(mylist))
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
print(mylist.count(3))
print(mylist.count(2))
mystr= "Quick Step Bangalore"
print(mystr[6:10])
print(mystr[-9:])
print(mystr[:15:11])
'''


'''
4)write a python program to evaluate below String
a)Add the string " RT Nagar "  and print the new string
b)Find the length of the string and reverse it
'''

'''
mystr= "Quick Step Bangalore"
print(mystr+" RT Nagar")
print(mystr[::-1])
print(mystr)
print(len(mystr))
'''

'''


5)List Slicing 
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
write a python program to slice the mylist
a)print elements [1,2,3] using slicing concept
b)print elements [9,0,122,10,2,3] 
c)print elements [8,1,2,3,9,0,122,10,2,3,4,3,3,2] 
d)print elements [10,2,3,4,3,3,2]
e)print elements [10,3,3,2]
f)print elements [6,8,2,9]
g)print elements [1,0,3,2]

using negative slice 
e)print elements [10,3,3,2]
f)print elements [6,8,2,9]
g)print elements [1,0,3,2]
h)print elements [1,2,3,9,0,122]
'''
'''
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
print(mylist[6:9])
print(mylist[9:15])
print(mylist[5:])
print(mylist[12:])
print(mylist[12::2])
print(mylist[3:10:2])
print(mylist[6::4])
print(mylist[-7::2])
print(mylist[-16:-8:2])
print(mylist[-13::4])
print(mylist[-13:-7])

'''