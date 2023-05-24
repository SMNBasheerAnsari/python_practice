#conditional_controle_statemetns
'''
#anagrams
f=input("enter a string:")
s=input("enter a string:")
print(f,s)
sf=sorted(f)
ss=sorted(s)
if sf==ss:
    print('these two strings are anagrams')
else:
    print('these two strings are not anagrams')
'''
'''
#leap_year
y=int(input('enter a year to check leep_year or not:'))
if y%400==0 or (y%100!=0 and y%4==0):
    print(f'given year {y} is a leep year')
else:
    print(f'given year {y} is not a leep year')
'''
'''
#max_of_3
a=int(input('enter A value:'))
b=int(input('enter B value:'))
c=int(input('enter C value:'))
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
'''
'''
#max_of_3_strings
a=input('enter a charecter:')
b=input('enter a charecter:')
c=input('enter a charecter:')
if a>b and a>c:
    print(ord(a),a)
elif b>c:
    print(ord(b),b)
else:
    print(ord(c),c)
'''
'''
#max_of_5_num
a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter a number:'))
d=int(input('enter a number:'))
e=int(input('enter a number:'))
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
    else:
        if c>d:
            if c>e:
                print(c)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
else:
    if b>c:
        if b>d:
            if b>e:
                print(b)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
    else:
        if c>d:
            if c>e:
                print(c)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
'''
'''
#sum of elements of a list by lambda and reduce
l=[1,2,3,4,5,6,7,8,9]
import functools
print(functools.reduce(lambda x,y:x+y,l))
'''
'''
l=(input('input a list').split())
l1=(list(filter(lambda x:x==x[::-1],l)))
print(list(map(int,l1)))
'''
'''
#emrip
m=int(input(':'))

def revers(n):
    reverse=0
    for i in range(len(str(n))):
        reminder=n%10
        reverse=reverse*10+reminder
        n//=10
    return reverse

def prime(a):
    if a>1:
        for i in range(2,a//2+1):
            if a%i==0:
                return False
        else:
            return True
    else:
        return False
c=0
for i in range(10,20000):
    if prime(i) and prime(revers(i)):
        c+=1
    if c==m+1:
        print(i)
        break
'''
'''
#odd even elements of string
s='abcdefghijklmnopqrstuvwxyz'
print('odd places')
for i in range(0,len(s),2):
    print(s[i],end=' ')
print()
print('even places')
for i in range(1,len(s),2):
    print(s[i],end=' ')
'''
'''
#odd even numbers
print('odd numbers')
for i in range(1,10,2):
    print(i)
print('even numbers')
for i in range(0,10,2):
    print(i)
'''
'''
#counting a sub string
s='hala halaha hahalaha'
sub='la'
c=0
for i in range(len(s)-len(sub)+1):
    if s[i:i+len(sub):1]==sub:
        c+=1
        print(i,i+len(sub),s[i:i+len(sub):1])
print(c)
'''
'''
#reversing a string
s=input('enter a string:')
rev=''
for i in range(1,len(s)+1):
    rev+=s[-i]
print(s)
print(rev)
'''
'''
#counting words of a string
s=input('enter a string:')
c=0
for i in range(len(s)):
    if s[i]==' ':
        c+=1
print(c+1)
'''
'''
#perfect numbers 
n=int(input('enter a value:'))
summ=0
for i in range(1,n//2+1):
    if n%i==0:
        summ+=i
if n==summ:
    print(n,'is a perfect number')
else:
    print(n,'is not a perfect number')
'''
'''
#perfect numbers in a given range
for i in range(1,1000):
    summ=0
    for j in range(1,i//2+1):
        if i%j==0:
            summ+=j
    if i==summ:
        print(i)
'''
'''
#nth perfect number:
n=int(input('enter nth value:'))
c=0
i=1
while True:
    summ=0
    for j in range(1,i//2+1):
        if i%j==0:
            summ+=j
    if i==summ:
        c+=1
    if c==n:
        print(i)
        break
    i+=1
'''
'''
#prime numbers
n=int(input('enter a value:'))
for i in range(2,n//2+1):
    if n%i==0:
        print('not a prime number')
        break
else:
    print(n,'is a prime numbers')
'''
'''
#prime numbers in a given range
for i in range(2,1000):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)
'''
'''
#nth prime number:
n=int(input('enter nth value:'))
c=0
i=2
while True:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        c+=1
    if c==n:
        print(i)
        break
    i+=1
'''
'''
#febinocy series
n=int(input('enter n value:'))
f=int(input('enter f value:'))
s=int(input('enter s value:'))
l=[]
l.append(f)
l.append(s)
summ=0
for i in range(n-2):
    summ=f+s
    l.append(summ)
    f,s=s,summ
#print(l)
e=l[0:len(l):2]
o=l[-2:-len(l):-2]
print(e,o)
'''
sp=0
st=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(v,end=' ')
    if i<n//2:
        sp+=1
    else:
        sp-=1
    print()
   
        











    
