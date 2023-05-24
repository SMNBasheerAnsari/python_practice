s=input('enter string')
for i in s:
    if i!=' ':
        print(i,end='')
    else:
        print('')
    
'''
s=input('enter string')
L=[]
new=''
for i in range(len(s)):
    if s[i]==' ':
        L+=[new]
        new=''
    else:
        new+=s[i]
    if i==len(s)-1:
        L+=[new]
print(L)
'''
