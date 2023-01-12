class GrandParents:
    gname='grand parents'

class Parent(GrandParents):
    name='Parents'
    def greeting(a):
        print('good evening')


class Child(Parent):
    child='child class'

    def greetingsChild(self):
        print('i am a child wishing u good night')


obj1=Parent()
obj1.greeting()
print(obj1.name)

obj2=Child()


print('\n')
print(obj2.child)
print(obj2.name)

obj2.greeting()
obj2.greetingsChild()
print(obj1.gname)
print(obj2.gname)