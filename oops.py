
class Bank:
    #geniric properties
    bank_name='sbi'
    bank_roi=7
    bank_branch='skht'
    bank_manager='sai'
    bank_employees=10

    #specific properties
    def __init__(self,nm,ag,gd,ac,bal):
        self.name=nm
        self.age=ag
        self.gender=gd
        self.account=ac
        self.balance=bal

    #object methods
    def display_specific(self):
        print('object address',self)
        print('name',self.name)
        print('age',self.age)
        print('gender',self.gender)
        print('account',self.account)
        print('balance',self.balance)

    def withidraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print('withidral sucessfull')
            print('your current balance is:',self.balance)
        else:
            print('insuficient balance, check again')
            print('your current balance is:',self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print('deposit completed,thank you')
        print('your current balance is:',self.balance)
    
    #class methods by useing decoraters
    @classmethod
    def display_geniric(cls):
        print('class address',cls)
        print('bank name:',cls.bank_name)
        print('bank rate of intrest:',cls.bank_roi,'%')
        print('bank branch name:',cls.bank_branch)
        print('bank ifsc no:',cls.bank_ifsc)
        print('bank manager name:',cls.bank_manager)
        print('no of employees:',cls.bank_employees)

    @classmethod
    def modify_GP(cls):
        print('change your bank branch here')
        newbranch=cls.get_string()
        cls.bank_branch=newbranch
        print('branch name is modified')
        print(cls.bank_branch)
        
        print('change your bank rate of intrest here')
        newroi=cls.get_integer()
        cls.bank_roi=newroi
        print('bank rate of intrest is modified')
        print(cls.bank_roi,'%')

    #static methods
    @staticmethod
    def get_string():
        string=input('string:')
        return string

    def get_integer():
        integer=int(input('integer:'))
        return integer

Bank.bank_ifsc='sbi000851'#creating new geniric property by using class

Bank.display_geniric()#calling class method by useing class

priya=Bank('priya',22,'female',123456,987654)
print('priya object is reated')
print()

#priya.display_geniric()  #calling class method by using object
        
priya.display_specific()  #calling obj method by using object
print('priya specific properties')
#Bank.display_specific(priya)#calling obj method by using class and passing obj reference
print()

pin=int(input('enter ATM pin:'))
if pin==62814:
    print('select options')
    print('1.deposit','2.withidraw',sep='\n')
    option=int(input(':'))
    if option==1:
        amount=int(input('enter amount:'))
        priya.deposit(amount)
    elif option==2:
        amount=int(input('enter amount:'))
        priya.withidraw(amount)

priya.modify_GP()#modifing class method by using object

'''
l=[0,1,0,3,0,12]
for i in range(len(l)):
    if l[i]==0:
        l.append(l.pop(i))
print(l)
'''
'''
s=[0,1,0,3,0,12]
print(s)
s.sort(reverse=True)
print(s)
print(s.sort())
'''


