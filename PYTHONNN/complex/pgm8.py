#filter
# l1={1,2,3,4,5,6,7,8,9}
# l1=(1,2,3,4,5,6,7,8,9)
l1=[1,2,3,4,5,6,7,8,9]
l2=[1,2,4,7,10,11,12,34]
res=list(filter(lambda x:x not in l1,l2))
print(res)

l2=[1,2,4,7,10,11,12,34]
def greater(num):
    return num>5

c=list(filter(greater,l2))
print(c)
res=list(filter(lambda x: x < 5 , l2))
print(res)