'''
#A
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0 or i==n//2:
        N=n-1
        sp=0
    else:
        N=1
        sp=n-2
    for j in range(N):
        print('*',end=' ')
    for k in range(sp):
        print(' ',end=' ')
    for l in range(1):
        print('*',end=' ')
    print()
#B
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0 or i==n//2 or i==n-1:
        N=n-1
        sp=0
    else:
        N=1
        sp=n-2
    for j in range(N):
        print('*',end=' ')
    for k in range(sp):
        print(' ',end=' ')
    for l in range(1):
        print('*',end=' ')
    print()
#C
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0 or i==n-1:
        N=n
    else:
        N=1
    for j in range(N):
        print('*',end=' ')
    print()
#D
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0 or i==n-1:
        N=n-1
        sp=0
        L=0
    else:
        N=1
        sp=n-2
        L=1
    for j in range(N):
        print('*',end=' ')
    for k in range(sp):
        print(' ',end=' ')
    for l in range(L):
        print('*',end=' ')
    print()
#E
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0 or i==n-1:
        N=n
        sp=0
    elif i==n//2:
        N=n-1
        sp=0
    else:
        N=1
        sp=n-2
    for j in range(N):
        print('*',end=' ')
    for k in range(sp):
        print(' ',end=' ')
    print()
#F
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0:
        N=n
        sp=0
    elif i==n//2:
        N=n-1
        sp=0
    else:
        N=1
        sp=n-2
    for j in range(N):
        print('*',end=' ')
    for k in range(sp):
        print(' ',end=' ')
    print()
'''
#G?
n=int(input('enter valu(>3):'))
for i in range(n):
    if i==0 or i==n-1:
        N=n
        sp=0
        S=1
    elif i==n//2:
        sp=0
        S=0
    else:
        N=1
        sp=n-2
        S=0
    if i>n//2:
        M=1
    else:
        M=0
    for s in range(S):
        print(' ',end=' ')
    for j in range(N):
        print('*',end=' ')
    for k in range(sp):
        print(' ',end=' ')
    for m in range(M):
        print('*',end=' ')
    print()



