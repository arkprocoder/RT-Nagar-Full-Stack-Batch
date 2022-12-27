'''1)create a list mylist  
add "apple","banana","orange","mosambi"
a)append "pineapple"
b)remove "orange" and find the length of list
c)print "banana, mosambi, pineapple"

d)add new list to the existing [1,2,3,4]
e)print only [1,2,3,4] and reverse [4,3,2,1]'''

mylist=["apple","banana","orange","mosambi"]
mylist.append("pineapple")
print(mylist)
mylist.remove("orange")
print(mylist)
print(len(mylist))
mylist.append([1,2,3,4])
print(mylist)
mylist[-1].reverse()
print(mylist[-1])