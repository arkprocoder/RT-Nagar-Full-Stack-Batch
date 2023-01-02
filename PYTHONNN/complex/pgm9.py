#reduce
from functools import reduce

l1=[1,2,3,4,5,6,7]
res=reduce(lambda x,y:x*y,l1)
print(res)
#outputis int