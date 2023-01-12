class Employee:
    company='tcs'
    def __init__(self,eName,eAge,eRole,eSalary):
        self.name=eName
        self.age=eAge
        self.role=eRole
        self.salary=eSalary
        # print('i have set all the values')
        # print(self.salary)
    
    @staticmethod
    def greetings():
        print("good evening")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company=newCompany


    def employeeDetails(self):
        localName='Bangalore'
        return f'\n {localName} \nCompany : {self.company} \nEmployee Details:\nEmployee Name is : {self.name}\nEmployee Age : {self.age}\nEmployee Role : {self.role}\nEmployee Salary : {self.salary}'
    
obj1=Employee('ark',25,'full stack dev',25000)
print(obj1.employeeDetails())
# obj1.greetings()

Employee.greetings()

obj2=Employee('rohan',25,'front end dev',250000)
newCompany='Infosys'
obj2.changeCompany(newCompany)
print(obj2.employeeDetails())