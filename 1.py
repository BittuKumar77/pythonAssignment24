# Write a python program to create a user class with 3 properties : name, age, email

class user:

    def __init__(self):
        self.name="Bittu"
        self.age=20
        self.email="bittuboss128@gmail.com"
    
    def get_data(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Email:",self.email)

p1=user()

p1.get_data()