#print all the perfect numbers in a given range:-
s=int(input('enter starting range:'))
e=int(input('enter ending range:'))
for n in range(s,e):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if n==sum:
        print(n)
#print every second perfect numbers in a given range:-
s=int(input('enter starting range:'))
e=int(input('enter ending range:'))
c=[]
for n in range(s,e):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if n==sum:
        c.append(n)
print(c[1::2])
#print every second perfect numbers in a given range:-
s=int(input('enter starting range:'))
e=int(input('enter ending range:'))
c=[]
for n in range(s,e):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if n==sum:
        c.append(n)
print(c[2::3])

        


        
