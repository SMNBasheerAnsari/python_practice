a=input('enter')
c=0
for i in range(len(a)):
    if i==0:
        c=1
    elif a[i+1]==a[i]:
        c+=1
    else:
        c=0
print(c,a[i])
