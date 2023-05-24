s=input('enter a string:')
'''
# ed5c7bA96
l=[]
for i in s:
    l.append(i)
#print(l)
l1=[]
for i in l:
    if i.isdigit()==False:
        l1.append(i)
#print(l1)
l1=l1[::-1]
#print(l1)
st=''
c=0
for i in range(len(s)):
    if s[i].isdigit()==False:
        st+=l1[c]
        c+=1
    else:
        st+=s[i]
print(st)
'''       
l=[]   
for i in s:
    if i.isalpha():
        l.append(i)
c=1
st=''
for i in s:
    if i.isalpha():
        st+=l[-c]
        c+=1
    else:
        st+=i
print(st)
