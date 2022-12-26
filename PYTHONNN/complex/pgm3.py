'''
mylist=['arshad','sadiq','hashsham','yaseen','fardeen']
# # for i,j in mylist:
# #     print(i,j)

newList=enumerate(mylist,11)
print(type(newList))
print(newList)
newList=list(newList)
print(newList)

print(newList[4])

for i,j in newList:
    print(i,j)

'''

mytup=('a','b','c','d','e')
# mytup=['a','b','c','d','e']
# mytup={'a','b','c','d','e'}
print(mytup)
newTup=enumerate(mytup,1)
# newTup=set(newTup)
# print(newTup)
newTup=tuple(newTup)
# print(newTup)
# newTup=list(newTup)
print(newTup)

for i,j in newTup:
    print(i,j)

# newTup1=((1, 'a','A'), (2, 'b','B'), (3, 'c','C'), (4, 'd','D'), (5, 'e','E'))
# for i,j,k in newTup1:
#     print(i,j,k)