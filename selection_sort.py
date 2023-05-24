'''
s=input(":")
l=s.split()
r=[]
for i in l:
    r.append(i[::-1])
print(' '.join(r))

s=input(":")
r=[]
r=s.split()
for k in r:
    if k==k[::-1]:
        print(k)
            

s=input('str:')
sub=input('sub:')
for i in range(len(s)):
    if s[i:i+len(sub):]==sub:
        d=True
        
    else:
        d=False
if d:
    print('given sub string is present')
else:
    print('given sub string is not present')
    
 
l=eval(input(":"))
for i in l:
    d=len(i)
    for j in range(d-1):
        l.append(i.pop(j))
print(l)
'''
l=eval(input(":"))
for i in l:
    print(i)
    d=len(i)
    print(d)
    for j in range(d):
        print(j)
        l.append(i.pop(j))
