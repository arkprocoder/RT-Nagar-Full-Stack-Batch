# li=[1,2,3,4,5,10,30,40,60,140,150,185,187,100,122,455,501,34,35]

# for i in li:
#     if i>500:
#         break
    
#     else:
#         if(i>150):
#             continue
#         print(i)

#  Display numbers from -10 to -1 using for loop
# for i in range(1,11):
#     print(i)

# for i in range(-10,0):
#     print(i)

# # start = 25
# # end = 50
# # print("Prime numbers between", start, "and", end, "are:")

# # for num in range(start, end + 1):
# #     # all prime numbers are greater than 1
# #     # if number is less than or equal to 1, it is not prime
# #     if num > 1:
# #         for i in range(2, num):
# #             # check for factors
# #             if (num % i) == 0:
# #                 # not a prime number so break inner loop and
# #                 # look for next number
# #                 break
# #         else:
# #             print(num)

# # fabonicci series

# # first two numbers
# num1, num2 = 0, 1

# print("Fibonacci sequence:")
# # run loop 10 times
# for i in range(10):
#     # print next number of a series
#     print(num1, end="  ")
#     # add last two numbers to get next number
#     res = num1 + num2

#     # update values
#     num1 = num2
#     num2 = res



n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)


rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")