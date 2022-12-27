# problems

# 1: Calculate the multiplication and sum of two numbers if output is > 1000 return addition else multiplication.

'''
def multiplication_or_sum(num1, num2):
    
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        sum1=num1 + num2
        return sum1

# first condition
num1=int(input('enter the first number'))
num2=int(input('enter the second number'))
result = multiplication_or_sum(num1, num2)
print("The result is", result)
'''

# Exercise 2: Print the sum of the current number and the previous number
'''

previous_num = 0

# loop from 1 to 10
for current_val in range(5):
    x_sum = previous_num + current_val
    print(f'previous number is {previous_num} current number is {current_val}= sum is {x_sum}')
    # modify previous number
    # set it to the current number
    previous_num = current_val
'''

# Exercise 3: Print characters from a string that are present at an even index number
# mystr=input('enter the name::\n')
# print(mystr[1::2])

# Exercise 4: Remove first n characters from a string
'''
def remove_chars(word, n):
    print('Original string:', word)
    length_word=len(word)
    if(length_word>n):            
        x = word[n:]
        print(x)
    else:
        print('sorry')

name=input('enter the word::\n')
n=int(input('enter how many characters u want to remove::\n'))
remove_chars(name, n)
'''

# 5. Check if the first and last number of a list is the same
'''
mylist=[]
lenlist=int(input('enter the length of the list :\n'))
print(f'Add the  {lenlist} numbers')
for i in range(lenlist):
    val=int(input(f'add {i}th index value:\n'))
    mylist.append(val)
print('your new list is ready')
print(mylist)
print('now i am check first index and last index of the new list')
if(mylist[0]==mylist[-1]):
    print('values are same')
else:
    print('values are different')

'''

# Exercise 6: Display numbers divisible by 5 from a list

mylist=[]
lenlist=int(input('enter the length of the list :\n'))
print(f'Add the  {lenlist} numbers')
for i in range(lenlist):
    val=int(input(f'add {i}th index value:\n'))
    mylist.append(val)
print('your new list is ready')
print(mylist)
print('now i am checking the values which is divisible by 5')

outputlist=[]
for j in mylist:
    if(j%5==0):
        outputlist.append(j)

print('resultant list is ',outputlist)
    
