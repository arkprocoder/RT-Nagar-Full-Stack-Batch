class Employee:
    def __init__(self,eName,eAge,eRole,eSalary):
        self.name=eName
        self.age=eAge
        self.role=eRole
        self.salary=eSalary
        # print('i have set all the values')
        # print(self.salary)
    

    def greetings(self):
        print("good evening",self.name)


    def employeeDetails(self):
        print(f'Employee Details:\nEmployee Name is : {self.name}\nEmployee Age : {self.age}\nEmployee Role : {self.role}\nEmployee Salary : {self.salary}')
    


obj1=Employee('arshad',25,'AI Developer',50000)
obj2=Employee('ark',25,'Full Stack Developer',60000)
obj1.employeeDetails()
obj1.greetings()
obj2.employeeDetails()
obj2.greetings()

# for i in range(5):
#     name=input('enter your name :\n')
#     age=int(input("enter  your age :\n"))
#     role=input('enter your role :\n')
#     salary=int(input("enter  your salary :\n"))
#     obj=Employee(name,age,role,salary)
#     obj.employeeDetails()
    

