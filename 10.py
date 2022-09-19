# 10. Define a class Employee with instance object variables empid, name, salary. Write
# __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class employee:
    def __init__(self):
        self.input()
        self.empid
        self.name
        self.salary

    def input(self):
        self.empid=input("Enter id:\t")
        self.name=input('Enter name:\t')
        self.salary=int(input('Enter salary:\t'))

    def display(self):
        print('empid=',self.empid)
        print('Name=',self.name)
        print('Salary=',self.salary)

print('Fill emp1 details:')
emp1=employee()
print('\nFill emp2 details:')
emp2=employee()
print('\nFill emp3 details:')
emp3=employee()

print('\nemp1 details')
emp1.display()
print('\nemp2 details')
emp2.display()
print('\nemp3 details')
emp3.display()