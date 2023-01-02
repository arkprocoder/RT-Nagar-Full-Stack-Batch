#  Calculate the sum of all numbers from 1 to a given number

n=int(input('enter the number :\n'))
j=[]
for i in range(n+1):
    j.append(i)

res=sum(j)
print(res)
    

n=int(input('enter the number :\n'))
j=0
for i in range(n+1):
    j+=i #j=j+i

print(j)
    