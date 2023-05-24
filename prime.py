n=int(input('enter a num to check prime or not:'))
for i in range(2,n):
    if n%i==0:
        print('given no is not prime')
        break
else:
    print('given num is prime')
