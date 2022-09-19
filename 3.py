# 3. Write a python program to create 2 objects of the user class and assign different
# values.

class user:

    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def get_data(self):
        print(self.name)
        print(self.age)

p1=user("Rahul",20)
p2=user("Akku",21)

p1.get_data()
p2.get_data()