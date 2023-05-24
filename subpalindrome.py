'''
s=input(":")
sub=''
o=2
for i in range(len(s)-o+1):
    for j in range(len(s)):
        d=s[i:j+o:]
        if d==d[::-1]:
            if len(d)>1:
                print(d)
    o+=1
'''
'''
s=input(":")
sub=''
for i in range(len(s)):
    for j in range(len(s)):
        sub=s[i:j:1]
        if sub==sub[::-1] and len(sub)>1:
            print(sub)

s='3b2c2a1d4a'
str=''
c=0
for i in s:
    x=i
    if x.isdigit():
        c=int(x)
    else:
        str=str+x*c
print(str)
'''
s=input("enter a string:")
str=''
if s[1].isdigit():
    for i in range(1,len(s),2):
        str=str+s[i-1]*int(s[i])
else:
    for i in range(0,len(s),2):
        str=str+s[i+1]*int(s[i])
print(str)
    





















    
