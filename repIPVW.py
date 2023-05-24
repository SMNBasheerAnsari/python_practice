s=input()
v='aeiouAEIOU'
n=''
for i in range(len(s)):
    if s[i] in v:
        n+=str(i)
    else:
        n+=s[i]
print(n)
#removing vowels
m=''
for i in range(len(s)):
    if s[i] not in v:
        m+=s[i]
print(m)
#counting words
N=1
for i in s:
    if i==' ':
        N+=1
print(N)
        
