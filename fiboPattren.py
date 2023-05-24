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
M=e+o
print(M)

sp=0
st=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(M[i],end=' ')
    if i<n//2:
        sp+=1
    else:
        sp-=1
    print()
   
