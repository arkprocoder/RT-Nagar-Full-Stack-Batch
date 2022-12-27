# 1. Write a program to print the odd numbers from 1 to 100
# for i in range(1,101,2):
#     print(i)


# 2. Write a program to print the even numbers from 1 to 100

# for i in range(2,101,2):
#     print(i)

# 3. Write a program to print {20,40,60,80,100} using for loop

# for i in range(20,101,20):
#     print(i)

# 4.print the number 1 to 10 using while loop

# i=1
# while(i<=10):
#     print(i)
#     i=i+1

# i=0
# while(i<10):
#     i=i+1
#     print(i)
    
# 4b.print the numbers 1 to 100  and it should print only even numbers

# i=0
# while(i<100):
#     i=i+2
#     print(i) 

# 4c.print the numbers 1 to 100 and should print only odd numbers
#  and it should break the loop when value becomes 51

# i=-1
# while(i<99):
#     i+=2
#     print(i)
#     if i==51:
#         break
    
# 4d.

# i=0
# while(i<100):
#     i+=1 #i=i+1
#     if i==55:
#         continue
#     print(i)

'''

5. Write a program to print the tables from 1 to 10
take a input from user.

2 x 1= 2
..
..
2 x 10 =20

'''
'''
n=int(input("enter the table number which u like to print:\n"))
for i in range(1,11):
    print(f'{n} X {i} = {n*i}')
'''

'''

7.Take a inputs and Evaluate the expressions
a)Take the Students name
b)Take the student english marks
maths,science,social,kannada,hindi while taking the inputs it should be in tha range (0-100)
c)calculate the % and print

% <35% print fail and print the Grade 'f'
% >35% and <55% print just pass and print the Grade 'd'
% >55% and <60% print  pass and print the Grade 'c'
% >60% and <75% print  average and print the Grade 'b'
% >75% and <90% print  good and print the Grade 'a'
% >90% and <100% print  excellent  and print the Grade 'A+'

'''


name=input("enter the student name :\n")
eng=int(input("Enter eng  marks \n"))
kan=int(input("Enter kan marks \n"))
hin=int(input("Enter hin marks \n"))
social=int(input("Enter social marks \n"))
science=int(input("Enter science marks \n"))
math=int(input("Enter math marks \n"))
avg=(eng+kan+hin+social+science+math)/6
if(eng>0 and eng<=100 and kan>0 and kan<=100 and hin>0 and hin<=100 and social>0 and social<=100 and science>0 and science<=100 and math>0 and math<=100):
    if avg<35:
        print(f'You have failed\nYou got {avg} %\nGrade is f ')
    
    elif(avg>=35 and avg<55):
        print(f'You have just pass \nYou got {avg} %\nGrade is d ')
    
    elif(avg>=55 and avg<60):
        print(f'You have passed \nYou got {avg} %\nGrade is c ')
    
    elif(avg>=60 and avg<75):
        print(f'You have average \nYou got {avg} %\nGrade is b ')
    
    elif(avg>=75 and avg<90):
        print(f'You have good \nYou got {avg} %\nGrade is a ')
    
    elif(avg>=90 and avg<=100):
        print(f'You have excellent \nYou got {avg} %\nGrade is a+ ')

    else:
        pass

else:
    print("Dont give negative numbers or greater than hundred")