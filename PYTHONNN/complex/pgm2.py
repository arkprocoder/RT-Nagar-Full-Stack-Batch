a=int(input("enter the value a :\n"))
b=int(input("enter the value b :\n"))
try:
    c=a/b
    print(c)
except  Exception as err:
    print("errors occured is ",err)
if True:
    c=a/b
    print(c)
else:
    print("errors occured ")
