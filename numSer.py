'''
#palindrom
n=int(input(':'))
N=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if N==rev:
    print('given number is palindrom')
else:
    print('given number is not palindrom')


#reverse
N=int(input(':'))
rev=0
while N>0:
    r=N%10
    rev=rev*10+r
    N=N//10
print(rev)

#sum of individual digits
N=int(input(':'))
rev=0
while N>0:
    r=N%10
    rev=rev+r
    N=N//10
print(rev)

#revers
N=int(input(':'))
rev=0
while True:
    r=N%10
    rev=rev*10+r
    N=N//10
    if N==0:
        break
print(rev)

#armstrong
N=input(':')
L=len(N)
tem=int(N)
arm=0
while tem>0:
    r=tem%10
    arm=arm+r**L
    tem=tem//10
if arm==int(N): 
    print('is armsrong')
else:
    print('not armstong')

#arm range 1000
N=10
while N<=1000:
    L=len(str(N))
    tem=N
    arm=0
    while tem>0:
        r=tem%10
        arm=arm+r**L
        tem=tem//10
    if arm==N: 
        print(N)
    N+=1

#first T arm nos 
N=0
T=int(input(':'))
c=0
while True:
    L=len(str(N))
    tem=N
    arm=0
    while tem>0:
        r=tem%10
        arm=arm+r**L
        tem=tem//10
    if arm==N: 
        c+=1
        print(N)
    N+=1
    if c==T:
        break

#arm nos in a given range
S=int(input('S:'))
E=int(input('E:'))
N=S
while N<=E:
    L=len(str(N))
    tem=N
    arm=0
    while tem>0:
        r=tem%10
        arm=arm+r**L
        tem=tem//10
    if arm==N: 
        print(N)
    N+=1
    if N==E:
        break

#Tth arm no
T=int(input('S:'))
N=1
c=0
while True:
    L=len(str(N))
    tem=N
    arm=0
    while tem>0:
        r=tem%10
        arm=arm+r**L
        tem=tem//10
    if arm==N:
        c+=1
    N+=1
    if c==T:
        print(N)
        break

#arm nos in a given range of positions
S=int(input('S:'))
E=int(input('E:'))
N=0
c=0
while N<=E:
    L=len(str(N))
    tem=N
    arm=0
    while tem>0:
        r=tem%10
        arm=arm+r**L
        tem=tem//10
    if arm==N:
        c+=1
        if c>=S:
            print(N)
    N+=1
    if c==E:
        break
#chick disarjum
N=int(input(':'))
L=len(str(N))
tem=N
dis=0
while tem>0:
    r=tem%10
    dis=dis+r**L
    L-=1
    tem=tem//10
if dis==N: 
    print('is disarjum')
else:
    print('not disarjum')

#disarium in a given range
S=int(input('S:'))
E=int(input('E:'))
N=1
while N<=E:
    L=len(str(N))
    tem=N
    dis=0
    while tem>0:
        r=tem%10
        dis=dis+r**L
        L-=1
        tem=tem//10
    if dis==N: 
        print(N,'is disarjum')
    N+=1
    
#first T disarium
T=int(input('T:'))
N=1
c=0
while N>0:
    L=len(str(N))
    tem=N
    dis=0
    while tem>0:
        r=tem%10
        dis=dis+r**L
        L-=1
        tem=tem//10
    if dis==N:
        c+=1
        print(N)
    if c==T: 
        break
    N+=1
'''
#Nth disarium in a given range
T=int(input('T:'))
N=1
c=0
while N>0:
    L=len(str(N))
    tem=N
    dis=0
    while tem>0:
        r=tem%10
        dis=dis+r**L
        L-=1
        tem=tem//10
    if dis==N:
        c+=1
    if c==T: 
        print(N)
        break
    N+=1
'''
#Sth to Eth disarium
S=int(input('Sth:'))
E=int(input('Eth:'))
N=1
c=0
while True:
    L=len(str(N))
    tem=N
    dis=0
    while tem>0:
        r=tem%10
        dis=dis+r**L
        L-=1
        tem=tem//10
    if dis==N:
        c+=1
        if c>=S:
            print(N)
    if c==E: 
        break
    N+=1

# check harshad/niven
N=int(input(':'))
tem=N
sum=0
while N>0:
    r=N%10
    sum=sum+r
    N=N//10
if tem%sum==0:
    print('given number is harshad/Niven')
else:
    print('given number is not harshad/Niven')

#harshad no in a given range
S=int(input('S:'))
E=int(input('E:'))
N=S
while N<=E:
    tem=N
    sum=0
    while tem>0:
        re=tem%10
        sum+=re
        tem//=10
    if N%sum==0:
        print(N)
    N+=1

#first T harshad nos
T=int(input('T:'))
N=1
c=0
while N>0:
    tem=N
    sum=0
    while tem>0:
        re=tem%10
        sum+=re
        tem//=10
    if N%sum==0:
        c+=1
        print(N)
    if c==T:
        break
    N+=1

#Tth harshad nos
T=int(input('Tth:'))
N=1
c=0
while N>0:
    tem=N
    sum=0
    while tem>0:
        re=tem%10
        sum+=re
        tem//=10
    if N%sum==0:
        c+=1
    if c==T:
        print(N)
        break
    N+=1

#Sth to Eth harshad no
S=int(input('Sth:'))
E=int(input('Eth:'))
N=1
c=0
while N>0:
    tem=N
    sum=0
    while tem>0:
        re=tem%10
        sum+=re
        tem//=10
    if N%sum==0:
        c+=1
        if c>=S:
            print(N)
    if c==E:
        break
    N+=1
'''










