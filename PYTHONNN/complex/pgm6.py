# numbers={1,2,3,4,5,6,7}
# numbers=[1,2,3,4,5,6,7]
# numbers=(1,2,3,4,5,6,7)
# res=tuple(map((lambda x:x*2),numbers))
# res=list(map((lambda x:x*2),numbers))
# res=set(map((lambda x:x*2),numbers))
# print(res)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# functions=[square,cube]
# numbers=[2,4,6,8]

# for i in numbers:
#     res=list(map(lambda x:x(i),functions))
#     print(res)
def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplication(a,b):
    return a*b

def modulous(a,b):
    return a%b

def power(a,b):
    return a**b

def doublediv(a,b):
    return a//b

function=[addition,substraction,multiplication,division,modulous,doublediv,power]

j=5
for i in range(1,10001):
    res=list(map(lambda x:x(i,j),function))
    # 1st iteration
    # res=list(map(lambda x:addition(1,5),function))
    # res=list(map(lambda x:substraction(1,5),function))
    # res=list(map(lambda x:multiplication(1,5),function))
    # res=list(map(lambda x:division(1,5),function))
    # res=list(map(lambda x:modulous(1,5),function))
    # res=list(map(lambda x:doublediv(1,5),function))
    # res=list(map(lambda x:power(1,5),function))
    # second iteration
    # res=list(map(lambda x:addition(2,5),function))
    # res=list(map(lambda x:substraction(2,5),function))
    # res=list(map(lambda x:multiplication(2,5),function))
    # res=list(map(lambda x:division(2,5),function))
    # res=list(map(lambda x:modulous(2,5),function))
    # res=list(map(lambda x:doublediv(2,5),function))
    # res=list(map(lambda x:power(2,5),function))
    print(res)