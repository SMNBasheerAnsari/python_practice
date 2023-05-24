'''
n=1
for i in range(5):
    I=i
    for j in range(n):
        print(2**I,end=' ')
        I-=1
    print()
    n+=1
'''
n=int(input('number:'))
for i in range(n):
    for k in range(n):
        print(i,k,' ',end='')
        
    print()
