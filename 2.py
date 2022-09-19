# 2. Write a python program to create a user class with a method to greet the user.

class user:

    def __init__(self):
        self.name="Bittu"
    
    def greet(self):
        print('Good Morning',self.name)

p1=user()
p1.greet()