a=input("enter a word:")
b=0
for i in a:
    if i!="a" and i!='e' and i!='i' and i!='o' and i!='u':
        b=b+1
print(b)

b=0
for i in a:
    if i=="a" or i=='e' or i=='i' or i=='o' or i=='u':
        b=b+1
c=len(a)-b
print(c)

for i in a:
    if i!="a" and i!='e' and i!='i' and i!='o' and i!='u':    
        print(i)
