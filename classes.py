
class Institute():
    name='JSP'
    principal='ravish'
    address='old air force road'
    area='marathalli'
    class_rooms=145
    teaching_staff=10
    staff=5
    computers=6
    furnitures=400

    def __init__(self,n,a,g,s1,s2,s3):
        self.name=n
        self.age=a
        self.gender=g
        self.marks1=s1
        self.marks2=s2
        self.marks3=s3
        self.avg=(s1+s2+s3)//3
        print(f"{self.name}'s object created")

    def display_specific(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.marks1)
        print(self.marks2)
        print(self.marks3)
        print(self.avg)
        if self.marks1>35 and self.marks2>35 and self.marks3>35 and self.avg>35:
            print(f'{self.name} is passed in all subjects')
        else:
            print(f'{self.name} is failed')
                                                
                                            
meghana=Institute('meghana reddy',20,'female',40,50,36)
srujana=Institute('Srujana shetty',21,'female',79,67,49)


#outer funtion to display geniric properties
def display_gen(self):
    print('school_name',self.name)
    print('school_principal',self.principal)
    print('school_address',self.address)
    print('school_area',self.area)
    print('school_class_rooms',self.class_rooms)
    print('school_teaching_staff',self.teaching_staff)
    print('school_non_teaching_staff',self.staff)
    print('school_computers',self.computers)
    print('school_furniture',self.furnitures)
display_gen(Institute)

meghana.display_specific()
srujana.display_specific()

class Bank():
    bank_name='sbi'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f'{self.name} obj created')
    def display(self):
        print(self.name)
        print(self.age)
meghana1=Bank('meghana reddy',20)
meghana1.display()
print(meghana1.age)
