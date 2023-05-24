'''
#floyd's triangle
n=5
s=1
for i in range(n):
    d=i+1
    for j in range(s):
        print(d%2,end=' ')
        d-=1
    s+=1
    print()

#special numbers
n=int(input(':'))
tem=n
L=len(str(n))
d=0

for i in range(L):
    

l=eval(input('enter a list:'))
a=0
b=1
n=len(l)
for i in range(n//2):
    l[a],l[b]=l[b],l[a]
    a+=2
    b+=2
print(l)

n=int(input('enter rows:'))
for i in range(1,n+1):
    d=i
    for j in range(1,n+1):
        if j<=i:
            print(i,end=' ')
        else:
            d+=1
            print(d,end=' ')
    print()

n=int(input('enter rows:'))
for i in range(1,n+1):
    d=i+1
    for j in range(1,n+1):
        if j<=i:
            d-=1
            print(d,end=' ')
        else:
            d+=1
            print(d,end=' ')
    print()

L=eval(input("enter a list:"))
s=int(input("enter a value of summ"))
def eleSumm(l,summ):

    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==summ:
                print('values', l[i],l[j])
                print('index:',i,j)
eleSumm(L,s)
'''
'''
x = int(input(':'))
y = int(input(':'))
z = int(input(':'))
n = int(input(':'))
l=[]
for i in range(x):
    for j in range(y):
        for k in range(z):
            if i+j+k!=n:
                l.append([i,j,k])

print(l)

'''
'''
#sp numbers
LL=int(input(":"))
UL=int(input(":"))
N=int(input(":"))
c=0
for i in range(LL,UL+1,1):
    summ=0
    tem=i
    while i>0:
        rem=i%10
        fact=1
        for j in range(1,rem+1):
            fact=j*fact
        summ=summ+fact
        if summ==tem:
            c+=1 
            if c==N:
                print(summ)
        i=i//10   
'''
n=int(input(":"))
rem=0
rev=0
tem=n
#for i in range(len(str(n))):
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if tem==rev:
    print('palindrom')
else:
    print('not palindrom')


















