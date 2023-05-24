l=[[1,2,3],[4,5,6],[7,8,9]]
'''
#printing matrix
l=eval(input('enter a list of matrix:'))
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=' ')
    print()
'''
'''
#rotate CW the matrix 90 degress
#l=eval(input('enter a list of matrix:'))
for i in range(len(l)):
    n=len(l[i])
    for j in range(n):
        print(l[n-(j+1)][i],end=' ')# for every iteration first element is fixed and second element is changing
    print()

'''
'''
#rotatr ACW the matric 90 degress
for i in range(len(l)):
    n=len(l[i])
    for j in range(n):
        print(l[j][n-(i+1)],end=' ')# for every iteration first element is changing and second element is constent
    print()
'''
#l=eval(input('enter a list of matrix:'))
'''
s=0
a=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if i==0 or i==len(l)-1:
            s+=l[i][j]
    a=abs(s-a)
    print(s,a)
print(a)
'''
'''
first=0
last=0
n=3
for i in range(n):
    first+=l[0][i]
    last+=l[n-1][i]
print(abs(first-last))
'''
'''
first=0
last=0
n=3
for i in range(n):
    first+=l[i][0]
    last+=l[i][n-1]
print(first+last)

'''
'''
first=0
last=0
n=3
for i in range(n):
    first+=l[n//2][i]
    last+=l[i][n//2]
print(first+last)

'''
'''
first=0
last=0
n=3
for i in range(n):
    first+=l[i][i]    #diagnel
    last+=l[n-(i+1)][i] # or last+=l[i][n-(i+1)]   anti-diagnel    

print(first*last)

'''
'''
n=4
for i in range(n):
    for j in range(n):
        if i+j==n//2 or abs(i-j)==n//2 or i+j==3*(n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
s='python'
'''
x=''
i=0
while i<len(s):
    x=s[i]+x
    i+=1
print(x)

'''
'''
l=[]
x=''
i=-1
while i>=-len(s):
    x=x+s[i]
    l.append(x)
    i-=1
print(l)

'''
'''
s='google bleed bloodd'
d={}
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c=s.count(s[i:i+2:])
        d[s[i]]=c
if s[-2]==s[-1]:
    d[s[i]]=c
print(d)
'''
'''  
s='google bleed bloodd'
d={}
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        if c>1:
            if s[i] not in d:
                d[s[i]]=c//2
            else:
                d[s[i]]+=c//2
            c=1
if c>1:
    d[s[i+1]]=c//2
print(d)
'''
'''
def Lower(s):
    x=''
    for i in range(len(s)):
        if i in range(len(s)-3,len(s)):
            x+=s[i].lower()
        else:
            x+=s[i]
    print(x)
e=input('enter employee name:')
Lower(e)
'''
'''
class Employee:
    def __init__(self,n,a,g,ex):
        self.name=n
        self.age=a
        self.gender=g
        self.experiance=ex

    def Lower(self):
        self.x=''
        for i in range(len(self.name)):
            if i in range(len(self.name)-3,len(self.name)):
                self.x+=self.name[i].lower()
            else:
                self.x+=self.name[i]
        print(self.x,'get the job')
        print(self.name)

s=Employee('Sai subham Das',23,'male',5)
s.Lower()
'''
'''
s='sai'
for i in range(len(s)):
    s=s[1:len(s):1]+s[0]
    print(s)
'''
'''
def amstrong(n):   
        num=n
        add=0
        l=len(str(num))
        while num!=0:
            rem=num%10
            add+=rem**l
            num=num//10
            
        if add==n:
            return 'amrstrong'
        else:
            return 'not amrstong'
 
print(amstrong(153))   
'''    
'''
def amstrong(n):   
        num=n
        l=len(str(num))
        def number(n):
            nonlocal num,l
            add=0
            rem=num%10
            add+=rem**l
            num=num//10
            if num==0:
                return add
            number(num)
        if number(num)==n:
            return 'amrstong'
        else:
            return number(num)
 
print(amstrong(153))   
'''
'''
def remainder_loop(n): 
    rem=n%10
    print(rem)
    remainder_loop(n//10)
      
print(remainder_loop(153))
'''
#armstron in recursion
def armstrong(num,i):
    if num==0:
        return 0
    return (num%10)**i+armstrong(num//10,i)

#checking 5 no 
for i in range(5):
    num=int(input('enter a value to check is amtsrong or not:'))
    if num==armstrong(num,len(str(num))):
        print(num,'is a armstrong number')
    else:
        print(num,'is not a armstrong number')








