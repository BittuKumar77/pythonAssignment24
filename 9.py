# 9. Write a python program to create a School class and 3 instance variables and 1 class
# variable.

class school:
    school_name="DAV public school"

    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    
    def show_data(self):
        print('The name is:',self.name)
        print('The roll is:',self.roll)
        print('The marks is:',self.marks)
        print('The school name is:',school.school_name)

std1=school('Ankit',5,98)

std1.show_data()