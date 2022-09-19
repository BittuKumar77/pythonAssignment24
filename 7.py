# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
# hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
# values).

class laptop:

    def __init__(self,brand,ram,cpu,hdd ):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
        
    def showConfig(self):
        print('Brand is:',self.brand)
        print('Ram is: ',self.ram,'GB')
        print('Cpu is: ',self.cpu)
        print('Hdd is:',self.hdd)

lap1=laptop("Dell",12,'Radeon 5',500)
lap1.showConfig()