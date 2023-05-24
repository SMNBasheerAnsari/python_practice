st=input()
sub=input()
c=0
for i in range(len(st)):
    if st[i:i+len(sub):]==sub:
        c+=1
print(c)
