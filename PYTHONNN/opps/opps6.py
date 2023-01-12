class A:
    def food(self):
        print('food A')

class B(A):
    def food(self):
        print('food B')

    def drink(self):
        print('drink B')

class C(B):
    def food(self):
        print('food C')

class D(B):
    def food(self):
        print('food D')

    def drink(self):
        print('drink D')

class E(D):
    def food(self):
        print('food E')


obj=E()

obj.drink()
obj.food()
'''
# saqiq - 
drink b
food -d

#arshad
food a 
food B
drink B
food D
drink D
food E


hashram

drink B
food A


farden

drink B
drink D
food A
food B
food D
food E




'''
