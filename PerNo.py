n=int(input("enter a number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print(n)
print(sum)
if sum==n:
    print('given number is perfect number')
else:
    print('given number is not perfect number')

            
