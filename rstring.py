st=input("enter a string:")
l=len(st)
ns=str()
for i in range(-1,-(l+1),-1):
    ns=ns+st[i]
print(ns)

for i in range((len(st)-1),-1,-1):
    ns=ns+st[i]
print(ns)

