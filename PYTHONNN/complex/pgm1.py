'''
mytup=1,2,3,4,5,6,7,8,9,10
print(mytup)
def functionArguments(args):
    print(args)
    for i in args:
        print(i)
    # print(args)
    print(type(args))

functionArguments(mytup)
'''
'''
mylist=[1,2,3,4,5,6,7,8,9,10]
# mylist={1,2,3,4,5,6,7,8,9,10}
# def functionArguments(*args,name): wrong way
def functionArguments(*args,name):
    for i in args:
        print(i)
        print(type(i))
    print(args)
    print(type(args))
    print(type(name))
    print(name)
# functionArguments("ark",mylist)
functionArguments(mylist,'ark')
'''
'''

# kwargs
mylist=[1,2,3,4,5,6,7,8,9,10]
mydict={
"name":"rohan",
"age":25,
"phone":7895463210,
"salary":7894.52
}
# print(mydict.items())
def keywordArgsFunction(name,*args,**kwargs):
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print("key is ",k,"value is ",v)
        print('testing')
    
    print(name,"good morning")

keywordArgsFunction("ark",mylist,mydict)


mydict2={
    'first':'Greeks',
    'mid':'for',
    'last':'Geeks'
}

def myFun(name,**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
myFun('ark',mydict2)

'''

def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 
 
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)
 
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(arg1='Geeks',arg2='for')
myFun(**kwargs)