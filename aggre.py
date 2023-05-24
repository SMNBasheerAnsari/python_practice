class Student:

    #specific properties
    def __init__(self,n,ag,gd,cl,add):
        self.name=n
        self.age=ag
        self.gender=gd
        self.clas=cl
        self.address=add

    #object methods
    def display_specific(self):
        print('name',self.name)
        print('age',self.age)
        print('gender',self.gender)
        print('class',self.clas)
        print('address',self.address)
        print()
        self.address.display_Address()

class Address:

    def __init__(self,c,dis,st,co):
        self.city=c
        self.district=dis
        self.state=st
        self.country=co

    def display_Address(self):
        print('city:',self.city)
        print('district:',self.district)
        print('state:',self.state)
        print('country:',self.country)
        print('#')
        print('self address',self)

class Trainer():
    def __init__(self,n,ag,gd,sub,c,dis,st,co):
        self.name=n
        self.age=ag
        self.gender=gd
        self.subject=sub
        AO=Address(c,dis,st,co)#creating obj to Address class
        self.address=AO

    def display_specific(self):
        print('name:',self.name)
        print('age:',self.age)
        print('gender:',self.gender)
        print('subject:',self.subject)
        print()
        self.address.display_Address()

h=Trainer('name','age','gender','subject','city','distric','state','country')
h.display_specific()
        
bnlr=Address('white filds','bangloor','karnataka','India')
print(bnlr)
rmpt=Address('rajampeta','kadapa','AP','India')
print(bnlr)

sai=Student('sai subham',20,'male','python',bnlr)
priya=Student('priya',20,'female','java',rmpt)

sai.display_specific()
print()
Student.display_specific(priya)
print()

skht=Address('sri kalahasti','tirupati','AP','India')
Address.display_Address(skht)

