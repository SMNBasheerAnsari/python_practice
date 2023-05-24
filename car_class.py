class Car():
    def __init__(self,m,c,b,g,f,s):
        self.model=m
        self.colour=c
        self.brand=b
        self.gare_system=g
        self.fuel_type=f
        self.strearing_side=s

    def start(self):
        print('car started')

    def acceleration(self):
        print('car accelarated')

    def brak(self):
        print('car in brak')

    def stop(self):
        print('car stoped')

class Driver():
    def __init__(self,n,a,g,e):
        self.name=n
        self.age=a
        self.gender=g
        self.experiance=e
        m=input('enter car model:')
        c=input('enter car colour:')
        b=input('enter car brand:')
        g=input('enter car gare system:')
        f=input('enter car fuel type:')
        s=input('enter car stearing side:')

        OBJ=Car(m,c,b,g,f,s)
        self.car=OBJ

    def driving(self):
        self.car.start()
        self.car.acceleration()
        self.car.brak()
        self.car.stop()
        
p=Driver('person','age','gender','experiance')
p.driving()
        
