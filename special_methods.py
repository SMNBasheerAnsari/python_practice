class company():
    com_name='HVPl'
    com_ceo='harshad vali'
    com_emp_count=0

    def __init__(self,n,i,q,e):
        self.name=n
        self.id=i
        self.qual=q
        self.exp=e
        print(self.name,'is joined as a employee')
        company.com_emp_count+=1

    def __str__(self):
        return self.name

    def __del__(self):
        print(self.name,'is quit the job')

        company.com_emp_count-=1

sai=company('sai subham das',1230,'btech',3)
print('company employee count is ',company.com_emp_count)

bala=company('bala subramanyam',1231,'mtech',4)
print('company employee count is ',company.com_emp_count)

del sai
print('company employee count is ',company.com_emp_count)
