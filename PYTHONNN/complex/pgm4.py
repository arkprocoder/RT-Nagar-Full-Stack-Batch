# Join= it is function which can iterate list
# tuple and dictionary using .join using a seprator values like
# ,@,/,(), etc but it should of same data types before joining it

# list

# mylist=['arshad','sadiq','hashsham','yaseen','fardeen']
# seprator='/'
# res=seprator.join(mylist)
# print(res)
# print(type(res))

# #tuple
# mytup=("mahonar","sriram","bhanu","mahesh","abhishek")
# seprator="@"
# res=seprator.join(mytup)
# print(res)
# print(type(res))

# #dictionary
mydict={"employeName":"Anees","employeeSalary":'12345',"isActive":'True'}
seprator="#"
newmydict=seprator.join(mydict.values())
# newmydict=seprator.join(mydict.keys())
# newmydict=seprator.join(mydict)
print(newmydict)
print(newmydict.split('#'))

mystr='anees.rehman.khan'
mystr2='anees rehman khan'
mystr3='anees,rehman,khan'
print(mystr.split('.'))
print(mystr2.split(' '))
print(mystr3.split(','))