n=int(input('enter a value to print table:'))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
n=int(input('enter the number'))
s=n
st=1

for i in range(1,n+1):
    for i in range(s):
        print('',end='')
    d=65
    for i in range(st):
        print(chr(d),end='')
        d+=1
    s-=1
    st+=1
    print()
