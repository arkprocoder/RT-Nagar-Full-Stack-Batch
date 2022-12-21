# sets
# myset=set()
# myset.add(1)
# myset.add(2)
# myset.add(2)
# myset.add(23)
# print(type(myset))
# print(myset)
# myset={12,2}
# print(type(myset))
# # sets
# myset={1,2,3,4,2,3,4,2,3,4,8,9,5,6,7}
# print(type(myset))
# print(myset)
# print(myset.add(10))
# print(myset)
# print(myset.pop())
# print(myset)
# print(myset.pop())
# print(myset)
# print(myset.pop())
# # print(myset)
# s2={1,2,3,4,11,12,13,14}
# print(myset.union(s2))
# print(myset.intersection(s2))
# myset.remove(15)


myset=set()
n=int(input("enter the length of the set :\n"))
for i in range(1,n+1):
    v=int(input(f"enter the {i} value to add in set :\n"))
    myset.add(v)

print("myset is ",myset)
print(len(myset))
print(myset.union({7,4,5,9,0,10}))
print(myset.intersection({7,4,5,9,0,10}))