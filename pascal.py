from math import factorial as f
n=5
for i in range(n):
    for j in range(n-i+1):
        print(' ',end=' ')
    for k in range(i+1):
        print(f(i)//(f(k)*f(i-k)),end='   ')
    print()
    
