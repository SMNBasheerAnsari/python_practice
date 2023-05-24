l=[2,84,9,12,121,5,0,175]
l=[2,84,121,0,12]
print(l)
print('>')

n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            print(l)
    print()
'''
print('<')
for i in range(n):
    for j in range(n-i-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
        print(l)
'''
