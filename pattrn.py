'''d=1
for i in range(1,8):
    for j in range(1,4):
        print(d,end=' ')
    d+=1
    print()

n1=int(input('enter a value:'))
s1=0
t1=n1
for i in range(n1):
    for j in range(s1):
        print(' ',end=' ')
    for k in range(t1):
        print('*',end=' ')
    s1+=1
    t1-=1
    print()

n2=int(input('enter a value:'))
s2=n2
t2=1
for i in range(n2):
    for j in range(s2):
        print(' ',end=' ')
    for k in range(t2):
        print('*',end=' ')
    s2-=1
    t2+=1
    print()

n3=int(input('enter a value:'))
t3=1
for i in range(n3):
    for k in range(t3):
        print('*',end=' ')
    t3+=1
    print()

n4=int(input('enter a value:'))
t4=n4
for i in range(n4):
    for k in range(t4):
        print('*',end=' ')
    t4-=1
    print()
   
n=int(input('enter a value:'))
m=n
sp=1
s=0
for i in range(n):
    for i in range(n):
        print('*',end=' ')
    for i in range(sp):
        print('_',end=' ')
    for i in range(s):
        print('_',end=' ')
    for i in range(n):
        print('*',end=' ')
    sp+=1
    s+=1
    n-=1
    print()
sp2=0
for i in range(m+1):
    for i in range(sp2):
        print('*',end=' ')
    for i in range(m):
        print('_',end=' ')
    for i in range(m):
        print('_',end=' ')
    for i in range(sp2):
        print('*',end=' ')
    sp2+=1
    m-=1
    print()

n=int(input(':'))
N=n
s=0
for i in range(1,n+1):
    for j in range(s):
        print(' ',end=' ')
    for k in range(N):
        print(i,end=' ')
    s+=1
    N-=1
    print()

n=int(input(':'))
N=n
s=0
for i in range(1,n+1):
    for j in range(s):
        print(' ',end=' ')
    for k in range(1,N+1):
        print(k,end=' ')
    s+=1
    N-=1
    print()

n=int(input(':'))
N=n
s=0
for i in range(1,n+1):
    for j in range(1,N+1):
        print(j,end=' ')
    for k in range(s):
        print(' ',end=' ')
    s+=1
    N-=1
    print()

n=int(input(':'))
N=n
s=0
for i in range(1,n+1):
    for j in range(1,N+1):
        print(i,end=' ')
    for k in range(s):
        print(' ',end=' ')
    s+=1
    N-=1
    print()

n=int(input(':'))
N=1
s=n
for i in range(1,n+1):
    for j in range(N):
        print(N,end=' ')
    for k in range(s-1):
        print('_',end=' ')
    s-=1
    N+=1
    print()


n=int(input(':'))
N=1
s=n
for i in range(1,n+1):
    for j in range(s-1):
        print(' ',end=' ')
    for k in range(N):
        print(N,end=' ')
    s-=1
    N+=1
    print()

n=int(input(':'))
N=1
s=n
for i in range(n):
    for i in range(N):
        print(N,end=' ')
    for i in range(s-1):
        print(' ',end=' ')
    N+=1
    s-=1
    print()

n=int(input(':'))
N=1
s=n
for i in range(n):
    for i in range(s-1):
        print(' ',end=' ')
    for i in range(N):
        print(N,end=' ')
    N+=1
    s-=1
    print()

n=int(input(':'))
N=1
s=0
for i in range(n):
    for i in range(n):
        print(N,end=' ,')
        N+=1
    for i in range(s):
        print(' ',end=' ')
    n-=1
    s+=1
    print()

n=int(input(':'))
N=1
s=0
for i in range(n):
    for i in range(s):
        print(' ',end=' ')
    for i in range(n):
        print(N,end='  ')
        N+=1
    n-=1
    s+=1
    print()

n=int(input(':'))
N=1
s=n
d=1
for i in range(n):
    for i in range(s-1):
        print('_,',end=' ')
    for i in range(N):
        print(d,end=' ')
        d+=1
    N+=1
    s-=1
    print()

n=int(input(':'))
N=1
s=n
d=1
for i in range(n):
    for i in range(N):
        print(d,end=' ')
        d+=1
    for i in range(s-1):
        print('_,',end=' ')
    N+=1
    s-=1
    print()

n=int(input(':'))
N=n
s=0
c=ord('A')
for i in range(1,n+1):
    for j in range(s):
        print(' ',end=' ')
    for k in range(N):
        print(chr(c),end=' ')
    s+=1
    N-=1
    print()
    c+=1

n=int(input(':'))
N=n
s=0
c=ord('A')
for i in range(n):
    for k in range(N):
        print(chr(c),end=' ')
    for j in range(s):
        print(' ',end=' ')
    s+=1
    N-=1
    print()
    c+=1
'''
'''
n=int(input(':'))
sp=n//2
st=1
for i in range(n):
    for j in range(sp):
        print('_',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    if i<n//2:
        sp-=1
        st+=1
    else:
        sp+=1
        st-=1
    print()
'''
'''
n=int(input(':'))
sp=n//2
st=1
for i in range(n):
    num=st//2+1
    for j in range(sp):
        print('_',end=' ')
    for k in range(st):
        print(num,end=' ')
        if k<st//2:
            num-=1
        else:
            num+=1
    if i<n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2
    print()
'''
'''
n=int(input(':'))
sp=0
st=1
d=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(d,end=' ')
    if i<n//2:
        sp+=1
        d+=2
    else:
        sp-=1
        if d%2==1:
            d-=1
        else:
            d-=2
    print()

'''
'''
#V
n=int(input(':'))
sp=0
st=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    for l in range(((n-i)*2)-3):
        print(' ',end=' ')
    for m in range(st):
        if i!=n-1:
            print('*',end=' ')
    print()
    sp+=1
'''
'''
#>N
n=int(input(':'))
o,e=[],[]
for i in range(1,n+1):
    if i%2==1:
        o.append(i)
    else:
        e.append(i)
L=o+e[::-1]
sp=0
st=1
for r in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for c in range(st):
        print(L[r],end=' ')
    if r<n//2:
        sp+=1
    else:
        sp-=1
    print()
'''
'''
#>prim
n=int(input(':'))
L=[]
for i in range(1,n+1):
    for j in range(2,i//2+1):
        if i%j!=0:
            L.append(i)
print(L)
'''
'''
#^
n=int(input(':'))
sp=n-1
st=1
for i in range(n):
    d=i+65
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(chr(d),end=' ')
        if k<st//2:
            d-=1
        else:
            d+=1
    sp-=1
    st+=2
    print()
'''
'''
#J,value
n=int(input(':'))
N=int(input('::'))

for i in range(n):
    v=1
    for j in range(N):
        print(j,v,end='  ')
    v+=1
    print()

'''
n=int(input('enter rows:'))
N=1
c=65
for i in range(n):
    for j in range(N):
        print(chr(c),end=' ')
    if i<n//2:
        N+=1
        c+=1
    else:
        N-=1
        c-=1
    print()






































