'''
#max of 5 numbers
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
d=int(input('enter 4th number:'))
e=int(input('enter 5th number:'))

#using if-elif
print('-using if-elif-')
if a>b and a>c and a>d and a>e:
    print(a,'is biggest number')
elif b>c and b>d and b>e:
    print(b,'is biggest number')
elif c>d and c>e:
    print(c,'is biggest number')
elif d>e:
    print(d,'is biggest number')
else:
    print(e,'is biggest number')

#using nested-if
print('-using nested-if-')
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a,'is biggest number')
            else:
                print(e,'is biggest number')
        else:
            if d>e:
                print(d,'is biggest number')
            else:
                print(e,'is biggest number')
    else:
        if c>d:
            if c>e:
                print(c,'is biggest number')
            else:
                print(e,'is biggest number')
        else:
            if d>e:
                print(d,'is biggest number')
            else:
                print(e,'is biggest number')
else:
    if b>c:
        if b>d:
            if b>e:
                print(b,'is biggest number')
            else:
                print(e,'is biggest number')
        else:
            if d>e:
                print(d,'is biggest number')
            else:
                print(e,'is biggest number')
    else:
        if c>d:
            if c>e:
                print(c,'is biggest number')
            else:
                print(e,'is biggest number')
        else:
            if d>e:
                print(d,'is biggest number')
            else:
                print(e,'is biggest number')
'''
'''
#max of 5 strings
a=input('enter 1st string:')
b=input('enter 2nd string:')
c=input('enter 3rd string:')
d=input('enter 4th string:')
e=input('enter 5th string:')

#using if-elif
print('-using if-elif-')
if a>b and a>c and a>d and a>e:
    print(a,'is biggest string')
elif b>c and b>d and b>e:
    print(b,'is biggest string')
elif c>d and c>e:
    print(c,'is biggest string')
elif d>e:
    print(d,'is biggest string')
else:
    print(e,'is biggest string')
'''
'''
#max of 5 cdt
print('enter same type of cdt,first elements')
a=eval(input('enter 1st cdt:'))
b=eval(input('enter 2nd cdt:'))
c=eval(input('enter 3rd cdt:'))
d=eval(input('enter 4th cdt:'))
e=eval(input('enter 5th cdt:'))

#using if-elif
print('using if-elif')
if a>b and a>c and a>d and a>e:
    print(a,'is biggest cdt')
elif b>c and b>d and b>e:
    print(b,'is biggest cdt')
elif c>d and c>e:
    print(c,'is biggest cdt')
elif d>e:
    print(d,'is biggest cdt')
else:
    print(e,'is biggest cdt')
'''
'''
#print each and every element of CDT
cdt=eval(input('enter a CDT:'))
i=0
while i<len(cdt):
    print(cdt[i])
    i+=1
'''
'''
#max/min elements of CDT
cdt=eval(input('enter a homogenious CDT:'))
m=cdt[0]
n=cdt[0]
print('using for loop')
for i in range(len(cdt)):
    if m<cdt[i]:
        m=cdt[i]
    if n>cdt[i]:
        n=cdt[i]
print(m,'is max of CDT',n,'is min of CDT')

print('-using while loop-')
i=0
while i<len(cdt):
    if m<cdt[i]:
        m=cdt[i]
    if n>cdt[i]:
        n=cdt[i]
    i+=1
print(m,'is max of CDT',n,'is min of CDT')
'''
'''
#display CDT, len of elements as key:values as a dictionary
cdt=eval(input('enter a CDT:'))
d={}
for i in cdt:
    d[str(i)]=len(str(i))
print(d)   
'''
'''
v=str([10,20, 30])
print(v,len(v))
'''
'''
#max/min len of elements of CDT
cdt=eval(input('enter a CDT:'))
d={}
for i in cdt:
    d[str(i)]=len(str(i))
print(d)   

m=d[str(cdt[0])]
n=d[str(cdt[0])]
for i in d:
    if m<d[i]:
        m=d[i]
    if n>d[i]:
        n=d[i]

for i in d:
    if d[i]==m:
        print(i,'maximum length of CDT')
    if d[i]==n:
        print(i,'minimum length of CDT')    
'''
'''
#sorting the elements of string
s=input('enter a string:')
l=[]
for i in s:
    l.append(i)
print(l)
print('assending')
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
#print(l)
print(''.join(l))
print('dissending')
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(''.join(l))
'''
'''
#sorting elements of list 
c=eval(input('enter a LIST:'))
print('-using babool sort-')
for i in range(len(c)-1):
    for j in range(len(c)-1-i):
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
print('assending',c)
for i in range(len(c)-1):
    for j in range(len(c)-1-i):
        if c[j]<c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
print('dessending',c)

print('-using selection sort-')
for i in range(len(c)):
    m=i
    for j in range(i+1,len(c)):
        if c[j]<c[m]:
            c[j],c[m]=c[m],c[j]
print('assending',c)
for i in range(len(c)):

    for j in range(i+1,len(c)):
        if c[j]>c[i]:
            c[j],c[i]=c[i],c[j]
print('dessending',c)
'''
'''
t=(2,5,3,696,626,5489,723,3)
s={2,5,3,696,626,5489,723}
d={'s':40,'d':73,'a':305,'f':82,'g':23}

print(sorted(t))
print(sorted(s))
l=sorted(d)
for i in range(len(l)):
    print(d[l[i]])
'''
'''
#checking given NO is perfect or not
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
#printing perfect numbers in a given range
s=int(input('enter a staring value:'))
e=int(input('enter a ending value:'))
print('-using for loop-')
for n in range(s,e+1):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if n==summ:
        print(n,'is a perfect number')

print('-using while loop-')
n=s
while n<=e:
    summ=0
    i=1
    while i<n//2+1:
        if n%i==0:
            summ+=i
        i+=1
    if n==summ:
        print(n)
    n+=1
'''
'''
#printing first N perfect numbers
N=int(input('enter Nth place:'))
c=0
n=1
while n>0:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if n==summ:
        c+=1
        print(n,'is a perfect number')
    if c==N:
        break
    n+=1
print('-using nested while loop-')
k=0
n=1
while n>0:
    summ=0
    i=1
    while i<n//2+1:
        if n%i==0:
            summ+=i
        i+=1
    if n==summ:
        k+=1
        print(n,'is a perfect number')
    if k==N:
        break
    n+=1
'''
'''
#printing N perfect numbers
N=int(input('enter Nth place:'))
c=0
n=1
while n>0:
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    if n==summ:
        c+=1
    if c==N:
        print(n,'is a perfect number')
        break
    n+=1
print('-using nested while loop-')
k=0
n=1
while n>0:
    summ=0
    i=1
    while i<n//2+1:
        if n%i==0:
            summ+=i
        i+=1
    if n==summ:
        k+=1
    if k==N:
        print(n,'is a perfect number')
        break
    n+=1
'''
'''
#checking prime numbers
n=int(input('enter a value:'))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,'is not a prime number')
            break
    else:
        print(n,'is a prime number')
else:
    print(n,'is not a prime number')
print('-using while loop-')
i=2
while i<n//2+1:
    if n%i==0:
        print(n,'is not a prime number')
        break
    i+=1
else:
    print(n,'is a prime number')

'''
'''
#prime numbers in agiven range
s=int(input('enter a staring value:'))
e=int(input('enter a ending value:'))
n=s
while n<e:
    i=2
    while i<n//2+1:
        if n%i==0:
            break
        i+=1
    else:
        print(n,'is a prime number')
    n+=1

'''
'''
#first K prime numbers
k=int(input('enter K place'))
c=0
n=2
while True: 
    i=2
    while i<n//2+1:
        if n%i==0:
            break
        i+=1
    else:
        print(n,'is a prime number')
        c+=1
    if c==k:
        break
    n+=1
'''
'''
#Kth prime numbers
k=int(input('enter Kth value'))
c=0
n=2
while True: 
    i=2
    while i<n//2+1:
        if n%i==0:
            break
        i+=1
    else:
        c+=1
    if c==k:
        print(n,'is a prime number')
        break
    n+=1
'''
'''
#non prime numbers
s=int(input('enter a staring value:'))
e=int(input('enter a ending value:'))
n=s
while n<e:
    for i in range(2,n//2+1):
        if n%i==0:
            print(n,'is not a prime number')
            break
    n+=1
'''
'''
#first K non prime numbers
k=int(input('enter K place'))
c=0
n=2
while True: 
    i=2
    while i<n//2+1:
        if n%i==0:
            print(n,'is non-prime number')
            c+=1
            break
        i+=1
        
    if c==k:
        break
    n+=1
'''
'''
#swaping words of a string
s=input('enter a random word string:')
n=input('enter order of words to be:')
l=s.split()
st=''
for i in n:
    st+=l[int(i)]
    st+=' '
print(st)
'''
'''
#first n fibnocy serices  
f=int(input('enter f value:'))
s=int(input('enter s value:'))
n=int(input('enter nth position:'))
print(f)
print(s)
c=2
while True:
    d=f+s
    print(d)
    c+=1
    f,s=s,d
    if c==n:
        break
'''
'''
#fibnocy serices nth position
f=int(input('enter f value:'))
s=int(input('enter s value:'))
n=int(input('enter nth position:'))
c=2
while True:
    d=f+s
    c+=1
    f,s=s,d
    if c==n:
        print(d)
        break
'''
'''
def is_palindrom(n):
    num=n
    rev=0
    for i in range(len(str(num))):
        rem=num%10
        rev=rev*10+rem
        num//=10
    if n==rev:
        return True
    else:
        return False

def is_palindrom(n):
    num=str(n)
    rev=num[::-1]
    if n==int(rev):
        return True
    else:
        return False

def is_prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

N=int(input('enter Nth vaue:'))
n=10
c=0
while True:
    if is_prime(n) and is_palindrom(n):
        print(n)
        c+=1
    if c==N:
        break
    n+=1
'''
#> pattren:
#l=[1,2,3,5,8,13,21,34,55]
n=int(input('enter n value:'))
f=int(input('enter f value:'))
s=int(input('enter s value:'))
l=[]
l.append(f)
l.append(s)
summ=0
for i in range(n-1):
    summ=f+s
    l.append(summ)
    f,s=s,summ
print(l)

sp=0
st=1
d=0
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(l[d],end=' ')
    if i<n//2:
        sp+=1
        d+=2
    elif i==n//2:
        sp-=1
        d-=1
    else:
        sp-=1
        d-=2
    print()

















