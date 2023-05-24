'''
#printing non prime numbers in agiven range
st=int(input('starting:'))
en=int(input('ending:'))
for i in range(st,en+1):
    if st>1:
        for j in range(2,st//2+1):
            if i%j==0:
                print(i)
                break
'''    
#print febonacci series bw 0 to 50
f=int(input(':'))
s=int(input(':'))
print(f,s)
while True:
    a=f+s
    f=s
    if a>50:
        break
    print(a)
    s=a
    
            
