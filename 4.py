# 4. Write a python program to init default values for user object using __init__ method.

class  user:

    def __init__(self):
        user.course='Full Stack Web Development Using Python'
    
p1=user()
p2=user()

print(p1.course)
print(p2.course)