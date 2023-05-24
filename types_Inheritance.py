class HQ_SBI():
    bank_name='SBI'
    HQ_loc='Banglore'
    nu_branches=22000
    establish='1995'

    def __init__(self,n,a,g,p,e):
        self.name=n
        self.age=a
        self.gender=g
        self.pos=p
        self.exp=e

#single level inheritance
class SBI_HYBD(HQ_SBI):
    bank_branch='Hyderabad'
    bank_ifsc='70264'
    bank_roi=7.3

    def __init__(self,n,a,g,ac,b,p):
        self.name=n
        self.age=a
        self.gender=g
        self.acc=ac
        self.bal=b
        self.pin=p

    @classmethod
    def display_geniric(cls):
        print('Bank name is:',cls.bank_name)
        print('Bank HQ at:',cls.HQ_loc)
        print('Number of branches:',cls.nu_branches)
        print('Bank Established in:',cls.establish)
        print('Bank branch name is:',cls.bank_branch)
        print('bank ifsc code is:',cls.bank_ifsc)
        print('bank rate of intrest:',cls.bank_roi)

    @staticmethod
    def get_int():
        integer=int(input(':'))
        return integer

    def withdraw(self):
        print('Enter PIN')
        pin=self.get_int()
        if pin==self.pin:
            print('Enter amount to withdraw') 
            amount=self.get_int()
            if amount<=self.bal:
                self.bal-=amount
                print('withdral sucessful')
            else:
                print('insuficient balance')
        else:
            print('the entered pin is incurrect')

    def deposit(self):
        print('enter amount to deposit')
        amount=self.get_int()
        self.bal+=amount
        print('Amount deposited to account')

    def check_bal(self):
        print('enter PIN')
        pin=self.get_int()
        if pin==self.pin:
            print('current balance in your account is:',self.bal)
        else:
            print('incurrect pin')
    def customer_details(self):
        self.display_geniric()
        print('cusomer name:',self.name)
        print('cusomer age:',self.age)
        print('cusomer gender:',self.gender)
        print('cusomer account number:',self.acc)
        print('current balabce:',self.bal)

#Multi level inheritance
class RBI():
    def guidlines(self):
        print('''RBI Guidelines means any guideline, circular, notification, regulation, requirement or other restriction or any decision or determination relating to taxation, monetary union, capital adequacy norms and other prudential norms on income recognition, asset classification and provisioning pertaining to advances by banks and financial institutions, liquidity, reserve requirements, or reserve asset, special deposit cash ratio, or capital asset requirements or any other form of banking or monetary control issued or made by, or any interpretation, policy or administration of any of the foregoing, by any Competent Authority having jurisdiction over the matter in question, including any of these that has been or may be issued by the RBI in any manner connected with small finance banks in the private sector, whether in effect as of the date of the Agreement or hereafter.''')

    @staticmethod
    def get_int():
        integer=int(input(':'))
        return integer

    def bonds(self):
        print('welcome to GOVT finance')
        print('enter amount to invest in bonds')
        amount=self.get_int()
        if self.bal>=amount:
            self.bal-=amount
            print('sucessfully invested in bonds')
        else:
            print('enterd amount is morethan your current balance:')

class SBI_BNLR(HQ_SBI,RBI):
    bank_branch='Hyderabad'
    bank_ifsc='70264'
    bank_roi=7.3

    def __init__(self,n,a,g,ac,b,p):
        self.name=n
        self.age=a
        self.gender=g
        self.acc=ac
        self.bal=b
        self.pin=p

    @classmethod
    def display_geniric(cls):
        print('Bank name is:',cls.bank_name)
        print('Bank HQ at:',cls.HQ_loc)
        print('Number of branches:',cls.nu_branches)
        print('Bank Established in:',cls.establish)
        print('Bank branch name is:',cls.bank_branch)
        print('bank ifsc code is:',cls.bank_ifsc)
        print('bank rate of intrest:',cls.bank_roi)

    @staticmethod
    def get_int():
        integer=int(input(':'))
        return integer

    def withdraw(self):
        print('Enter PIN befour withdraw')
        pin=self.get_int()
        if pin==self.pin:
            print('Enter amount to withdraw') 
            amount=self.get_int()
            if amount<=self.bal:
                self.bal-=amount
                print('withdral sucessful')
                print('current balabce:',self.bal)
            else:
                print('insuficient balance')
        else:
            print('the entered pin is incurrect')

    def deposit(self):
        print('enter amount to deposit')
        amount=self.get_int()
        self.bal+=amount
        print('Amount deposited to account')
        print('current balabce:',self.bal)

    def check_bal(self):
        print('enter PIN to check balance')
        pin=self.get_int()
        if pin==self.pin:
            print('current balance in your account is:',self.bal)
        else:
            print('incurrect pin')
    def customer_details(self):
        self.display_geniric()
        print('cusomer name:',self.name)
        print('cusomer age:',self.age)
        print('cusomer gender:',self.gender)
        print('cusomer account number:',self.acc)
        print('current balabce:',self.bal)
    
'''
seetha=SBI_HYBD('SEETHA',23,'female',100,5000,23561)
print('seetha obj is crated to SBI HYBD')
seetha.display_geniric()
seetha.deposit()
seetha.withdraw()
seetha.check_bal()
seetha.customer_details()
'''

geetha=SBI_BNLR('GEETHA',20,'FEMALE',101,4000,53561)
print('geetha obj is created to SBI BNLR')
geetha.guidlines()
geetha.deposit()
geetha.check_bal()
geetha.withdraw()
geetha.customer_details()
geetha.bonds()
