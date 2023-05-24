'''
#1
n=int(input(':'))
N=1
s=n-1
for i in range(n):
    for j in range(N):
        print('*',end=' ')
    for k in range(s):
        print(' ',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#2
n=int(input(':'))
N=1
s=n-1
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print('*',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#3
n=int(input(':'))
N=n
s=0
for i in range(n):
    for j in range(N):
        print('*',end=' ')
    for k in range(s):
        print(' ',end=' ')
    N-=1
    s+=1
    print()
'''
'''
#4
n=int(input(':'))
N=n
s=0
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print('*',end=' ')
    N-=1
    s+=1
    print()
'''
'''
#5
n=int(input(':'))
for i in range(n):
    for k in range(n):
        if i==k:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
#6
n=int(input(':'))
s=n-1
N=1
for i in range(n):
    for j in range(s):
        print(' ',end=' ')
    for k in range(N):
        if k==0:
            print('*',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#7
n=int(input(':'))
for i in range(n):
    for k in range(n):
        if i==k:
            print('A',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
#10
n=int(input(':'))
s=n-1
N=1
for i in range(n):
    for j in range(s):
        print(' ',end=' ')
    for k in range(N):
        if k==0:
            print('M',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#11
n=int(input(':'))
N=1
s=n-1
for i in range(n):
    for j in range(N):
        print('A',end=' ')
    for k in range(s):
        print(' ',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#12
n=int(input(':'))
N=1
s=n-1
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print('B',end=' ')
    N+=1
    s-=1
    print()

'''
'''
#13
n=int(input(':'))
N=n
s=0
for i in range(n):
    for j in range(N):
        print('c',end=' ')
    for k in range(s):
        print(' ',end=' ')
    N-=1
    s+=1
    print()

'''
'''
#14
n=int(input(':'))
N=n
s=0
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print('D',end=' ')
    N-=1
    s+=1
    print()
'''
'''
#15
n=int(input(':'))
N=1
s=n-1
c=65
for i in range(n):
    for j in range(N):
        print(chr(c),end=' ')
        c+=1
    for k in range(s):
        print(' ',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#16
n=int(input(':'))
N=1
s=n-1
c=65
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print(chr(c),end=' ')
        c+=1
    N+=1
    s-=1
    print()
'''
'''
#17
n=int(input(':'))
N=n
s=0
c=65
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print(chr(c),end=' ')
        c+=1
    N-=1
    s+=1
    print()
'''
'''
#18
n=int(input(':'))
N=n
s=0
c=65
for i in range(n):
    for j in range(N):
        print(chr(c),end=' ')
        c+=1
    for k in range(s):
        print(' ',end=' ')
    N-=1
    s+=1
    print()
'''
'''
#19
n=int(input(':'))
N=1
s=n-1
for i in range(n):
    for j in range(N):
        print('1',end=' ')
    for k in range(s):
        print(' ',end=' ')
    N+=1
    s-=1
    print()
'''
'''
#20
n=int(input(':'))
N=1
s=n-1
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print('2',end=' ')
    N+=1
    s-=1
    print()

'''
'''
#21
n=int(input(':'))
N=n
s=0
for i in range(n):
    for j in range(N):
        print('3',end=' ')
    for k in range(s):
        print(' ',end=' ')
    N-=1
    s+=1
    print()

'''
'''
#22
n=int(input(':'))
N=n
s=0
for i in range(n):
    for k in range(s):
        print(' ',end=' ')
    for j in range(N):
        print('4',end=' ')
    N-=1
    s+=1
    print()
'''


'''
#last
n=int(input(':'))
sp=n-1
st=1
num=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    num=i+1
    for k in range(st):
        print(num,end=' ')
        if k<st//2:
            num-=1
        else:
            num+=1
            
    print()
    st+=2
    sp-=1
'''
'''
n=int(input(':'))
sp=n-1
st=1
char=65
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(chr(char),end=' ')
        if k<st//2:
            char-=1
        else:
            char+=1
    print()
    st+=2
    sp-=1

'''
#?
n=int(input(':'))
sp=0
st=n*2-1
for i in range(n):
    char=65
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(chr(char),end=' ')
        if k<st//2:
            char+=1
        else:
            char-=1
    st-=2
    sp+=1
    print()

'''
#>
n= int(input(':'))
sp=0
st=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
        
    for k in range(st):
        print('*',end=' ')
    if i<n//2:
        sp+=1
    else:
        sp-=1
    print()
'''















