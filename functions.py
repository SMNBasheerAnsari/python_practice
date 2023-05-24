'''
#prime
n=int(input(':'))
def isPrime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    else:
        return True
print(isPrime(n),n)
print(isPrime(2),2)
print(isPrime(3),3)
print(isPrime(4),4)
print(isPrime(91),91)
'''
'''
#emrip
n=int(input(":"))

def revers(n):
    reverse=0
    for i in range(len(str(n))):
        reminder=n%10
        reverse=reverse*10+reminder
        n//=10
    return reverse

def prime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    else:
        return True
rev=revers(n)
print(rev)
if prime(n) and prime(rev):
    print('emrip')
else:
    print('not emrip')

'''
'''
#special number
n=int(input(":"))
dummy=n
sum=0
def fact(a):
    result=1
    for i in range(1,a+1,1):
        result=result*i
    return result
    
for i in range(len(str(n))):
    reminder=n%10
    sum=sum+fact(reminder)
    n//=10
if dummy==sum:
    print('special number')
else:
    print('not a special number')
'''
'''
#perfect numbers
n=int(input(':'))

def divisors(a):
    l=[]
    for i in range(1,a//2+1):
        if a%i==0:
            l.append(i)
    return l
'''
'''
#1)printing number :-
N=int(input("enter a value:"))

def printing(a):
    print(a)

printing(N)

#2)printing numbers upto given number:-
N=int(input("enter a value:"))

def printing(a):
    print(a)

i=0
while i<=N:
    printing(i)
    i+=1

for i in range(N+1):
    printing(i)

#3)printing numbers in a given range:-
LL=int(input("enter LL value:"))
UL=int(input("enter UL value:"))

def printing(a):
    print(a)
    
for i in range(LL,UL+1):
    printing(i)

#4)printing Nth number in a given range :-
LL=int(input("enter LL value:"))
UL=int(input("enter UL value:"))
N=int(input("enter Nth value:"))
c=0

def printing(a):
    print(a)
    
for i in range(LL,UL+1):
    c+=1
    if c==N:
        printing(i)

#5)printing given number is positive or not :-
N=int(input("enter N value:"))

def isPositive(a):
    if a>0:
        print("given value is +ve number")
    elif a<0:
        print("given value is -ve number")
    else:
        print("given value is neither +ve or -ve")

isPositive(N)

#6)printing positive negitive numbers upto given numbers :-
N=int(input("enter N value:"))

def number(a):
    for i in range(a+1):
        print(i)
    for i in range(a+1):
        print("-",i)
number(N)

#7)printing positive negitive numbers upto given numbers :-
LL=int(input("enter LL value:"))
UL=int(input("enter UL value:"))

def number(a,b):
    for i in range(a,b+1):
        print(i)
    for i in range(a,b+1):
        print("-",i)
number(LL,UL)
'''
'''
n= 10
st=n
l=[]
for i in range(n):
    l+=[i]
    for j in range(st):
        print(j, end=' ')
        for m in range(len(l)):
            sp=0
            for o in range(sp):
                print(' ', end=' ')
            for a in range(st):
                print(m, end=' ')
                st-=1
            print()
'''
'''
LL=int(input("enter LL value:"))
UL=int(input("enter UL value:"))

def isReverse(n):
    reverse=0
    for i in range(len(str(n))):
        reminder=n%10
        reverse=reverse*10+reminder
        n//=10
    return reverse

def isPolindrome(n):
    rev=isReverse(n)
    if n==rev:
        return True
    else:
        return False

def isPrime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    else:
        return True

def isPolyprime(n):
    if isPolindrome(n) and isPrime(n):
        return True
    else:
        return False
def polyprime(a,b):
    for i in range(a,b+1):
        if isPolyprime(i):
            print(i)
polyprime(LL,UL)
 
LL=int(input("enter LL value:"))
UL=int(input("enter UL value:"))

def isPolyprime(n):
    num=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if num==rev:
        if num>1:
            for i in range(2,num//2+1):
                if num%i==0:
                    return True
            else:
                return False
        else:
            return False
    return False
    
def polyprime(a,b):
    for i in range(a,b+1):
        if isPolyprime(i):
            print(i)
polyprime(LL,UL)


def combination(x,y=25,*args,**kwargs):
    print(x,y)
    print(args)
    print(kwargs)
combination(25,30,25,45,a=45,b=45)

def outer():
    a,b=10,20
    print(a,b)
    def inner():
        print(a,b)
        #error in the time of complition it knows the error. when we call it through the error 
        a+=10
        b+=20
    inner()
    print(a,b)
a=50
b=100
outer()

#hallow squar
n=int(input(":"))
for i in range(n):
    if i==0 or i==n-1:
        st=n-2
        sp=0
    else:
        st=0
        sp=n-2
    for j in range(1):
        print('*',end=' ')
    for k in range(st):
        print('*',end=' ')
    for l in range(sp):
        print(' ',end=' ')
    for m in range(1):
        print('*',end=' ')
    print()
        
#hallow rectangle
n=int(input("ROWS:"))
m=int(input("COLUMN:"))
for i in range(n):
    if i==0 or i==n-1:
        st=m-2
        sp=0
    else:
        st=0
        sp=m-2
    for j in range(1):
        print('*',end=' ')
    
    for k in range(st):
        print('*',end=' ')
    for l in range(sp):
        print(' ',end=' ')
    for j in range(1):
        print('*',end=' ')
        
    print()

l=['aa:10','b:1','ccc:151']
l1=[]
for i in range(len(l)):
    l1.append(l[i].split(':'))
    l1[i][1]=int(l1[i][1])
print(dict(l1))
'''
'''
s='yybbBByyyyssssssss'
c=1
l=[]
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        l.append(c)
        c=1
l.append(c)
mx=max(l)
print(mx)
'''
'''
#recursion
N=int(input("enter a value to get the sum of the n natural numbers:"))
s=0
def summ(n):
    global s
    s=s+n
    if n==0:
        return s
    summ(n-1)
summ(N)
print(s)
'''
'''
N=int(input(':'))
def sDigit(n):
    while n>0:
        rem=n%10
        s+=rem
        n//=10
    return s
def harshad(n):
    if n%sDigit(n)==0:
        return True
    else:
        return False
print(harshad(N))
'''
'''
R=int(input("R:"))
C=int(input("C:"))

print('rectangle')
def rectangle(r,c):
    for i in range(r):
        for j in range(c):
            print('*',end=' ')
        print()
    
rectangle(R,C)

N=int(input('N:'))

print('squar')
def squar(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()
    
squar(N)
N=int(input('N:'))

print('Left triangle')
def triangle_Left(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()
        n-=1

triangle_Left(N)

N=int(input('N:'))

print('Left triangle')
def triangle_Left(n):
    st=1
    for i in range(n):
        for j in range(st):
            print('*',end=' ')
        print()
        st+=1

triangle_Left(N)


N=int(input('N:'))

print('Right triangle')
def triangle_right(n):
    sp=n-1
    st=1
    for i in range(n):
        
        for k in range(sp):
            print(' ',end=' ')
        
        for j in range(st):
            print('*',end=' ')
        print()
        sp-=1
        st+=1
triangle_right(N)


N=int(input('N:'))

print('Right triangle')

    
def triangle_right(n):
    sp=0
    st=n
    for i in range(n):
        
        for k in range(sp):
            print(' ',end=' ')
        
        for j in range(st):
            print('*',end=' ')
        print()
        sp+=1
        st-=1
triangle_right(N)

R=int(input("R:"))
C=int(input("C:"))

print('rectangle')
def rectangle(r,c):
    count=0
    for i in range(r):
        for j in range(c):
            print(count,end=' ')
        print()
        count+=1
rectangle(R,C)
'''
'''
def isReverse(n):
    reverse=0
        reminder=n%10
        reverse=reverse*10+reminder
        n//=10
    return reverse
'''
'''
N=int(input(":"))

def isPrime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    else:
        return True


def circularD(n):
    
    for i in range(len(str(n))):
        if isPrime(n):
            rem=n%10
            n//=10
            n=str(rem)+str(n)
            
        n=int(n)
    else:
        print('givenm number is a circular prime')
circularD(N)
'''
'''
def slantStar(n):
    sp=0
    for i in range(n):
        for j in range(sp):
            print(' ',end=' ')
        print('*')
        sp+=1
slantStar(6)
'''





















