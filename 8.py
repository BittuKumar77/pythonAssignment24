# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.

class laptop:

    def __init__(self,brand,ram,cpu,hdd ):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
        
    def showConfig(self):
        print('Brand is',self.brand)
        print('ram is ',self.ram,'GB')
        print('cpu is ',self.cpu)
        print('hdd is ',self.hdd)

    def create_sorted_list(self, lap2,lap3):
        lst=[lap1,lap2,lap3]
        lst2=[]
        for i in lst:
            lst2.append(i.ram)

        lst2.sort()
        lst3=[]
        for e in lst2:
            for k in lst:
                if e==k.ram:
                    lst3.append(k)      
        return lst3

lap1=laptop("Dell",12,'i5',"1tb")
lap2=laptop("hp",8,'Ryzen 5',None)
lap3=laptop("Asus",16,'i5',None)

sorted_list=lap1.create_sorted_list(lap2,lap3)

for e in sorted_list:
    print('The rams in sorted order is :',e.ram)

