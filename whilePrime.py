'''
#1 to 100 prime numbers
i=2
while i<=100:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)
    i+=1

#first 100 prime numbers
i=2
c=0
while i>1:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        c+=1
        print(i)
    
    if c==100:
        break
    i+=1
      
#1 to 1000 perfect numbers
n=1
while n<=10000:
    sum=0
    j=1
    while j<n//2+1:
        if n%j==0:
            sum+=j
        j+=1
    if n==sum:
        print(n)
    n+=1    

#Nth prime number
N=int(input(':'))
i=2
c=0
while i>1:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        c+=1
    
    if c==N:
        print(i)
        break
    i+=1
'''
#Nth perfect number
N=int(input(':'))
c=0
n=1
while n>0:
    sum=0
    j=1
    while j<n//2+1:
        if n%j==0:
            sum+=j
        j+=1
    if n==sum:
        c+=1    
    if c==N:
        print(n)
        break
    n+=1
    
   
