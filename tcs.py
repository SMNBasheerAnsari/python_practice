'''
S=input('enter a string:')
def missing(S):
    mis=''
    for i in range(97,123,1):
        if chr(i) not in S.lower():
            mis+=chr(i)
    return mis

ver=missing(S)
if ver==str():
    print(0)
else:
    print(ver)
'''
'''
MAX_CHAR = 26
def missingChars(Str):
    present = [False for i in range(MAX_CHAR)]
    for i in range(len(Str)): 
        if (Str[i] >= 'a' and Str[i] <= 'z'): 
            present[ord(Str[i]) - ord('a')] = True
        elif (Str[i] >= 'A' and Str[i] <= 'Z'): 
            present[ord(Str[i]) - ord('A')] = True

    res = ""
    for i in range(MAX_CHAR): 
        if (present[i] == False): 
            res += chr(i + ord('a')) 
    return res 

Str=input('enter a string:')

ver=missingChars(Str)
if ver==str():
    print(0)
else:
    print(ver)
'''
'''
# Python3 program to find characters  
# that needs to be added to make Pangram  

MAX_CHAR = 26

  
# Returns characters that needs  
# to be added to make str  

def missingChars(Str): 

      

    # A boolean array to store characters  

    # present in string.  

    present = [False for i in range(MAX_CHAR)] 

  

    # Traverse string and mark characters  

    # present in string.  

    for i in range(len(Str)): 

        if (Str[i] >= 'a' and Str[i] <= 'z'): 

            present[ord(Str[i]) - ord('a')] = True

        elif (Str[i] >= 'A' and Str[i] <= 'Z'): 

            present[ord(Str[i]) - ord('A')] = True

  

    # Store missing characters in alphabetic  

    # order.  

    res = "" 

  

    for i in range(MAX_CHAR): 

        if (present[i] == False): 

            res += chr(i + ord('a')) 

              

    return res 

  
# Driver code 

#Str = "The quick brown fox jumps over the dog"
Str=input('enter a string:')
  

ver=missingChars(Str)
if ver==str():
    print(0)
else:
    print(ver)
'''
'''
MAX_CHAR = 26
def missingChars(Str):
    present = [False for i in range(MAX_CHAR)]
    
    for i in range(len(Str)): 
        if (Str[i] >= 'a' and Str[i] <= 'z'): 
            present[ord(Str[i]) - ord('a')] = True
        elif (Str[i] >= 'A' and Str[i] <= 'Z'): 
            present[ord(Str[i]) - ord('A')] = True
    
    res = ""
    for i in range(MAX_CHAR): 
        if (present[i] == False): 
            res += chr(i + ord('a')) 
    return res 

Str=input('enter a string:')

ver=missingChars(Str)
if ver==str():
    print(0)
else:
    print(ver)
'''
'''
n=int(input('enter n value:'))

sp=n//2
st=1
d=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        if k==0 or k==st-1:
            print(d,end=' ')
            
        else:
            print(' ',end=' ')
    if i<n//2:
        sp-=1
        st+=2
        d+=1
    else:
        sp+=1
        st-=2
        d-=1

    print()
'''
'''

l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)):
    for j in range(1,len(l[i])+1):
        print(l[-j][i],end=' ')
    print()

'''
'''
s='PyTHon@123'
st=''
for i in s:
    if ord(i) in range(65,92):
        st+=chr(ord(i)+32)
    elif ord(i) in range(97,123):
        st+=chr(ord(i)-32)
    else:
        st+=i
print(st)
'''
'''
def series(s,e,u=1):
    for i in range(s,e,u):
        yield i
s=series(1,10,2)
for i in s:
    print(i)
'''
'''
sm=0
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

def sfact(n):
    global sm
    rem=n%10
    sm+=fact(rem)
    if n//10!=0:
        return sm


n=145
if sfact(n)==n:
    print("special")
else:
    print("not special")
    print(sfact(n))

'''
'''
n=int(input("enter n"))
n=25
def coin(n):
    s=0
    i=0
    while i<=n:
        s+=i
        if s<=n:
            i+=1
        else:
            return s,i
            break
v=coin(n)
if v[0]<=n:
    print(v[1])
else:
    print(v[1]-1)
'''
'''
n=10
v=(n/2)*(2a + (n – 1)d)
print(v)
'''
'''
n=list(map(int,input().split()))
l=list(map(int,input("pockmans").split()))
print(n,l)
def pocke(n):
    s=0
    for i in range(n[0]):
        s+=l[i]
        if i==n[1]-1:
            return s
        l[i-1]=0
        for j in range(len(l)):
            l[j]+=1    
print(pocke(n))

'''
'''
s=input("enter string")
st=''
N=int(input("enter integer"))
n=len(s)//N
i=0
while i<len(s):
    st+=s[i:i+n:1]
    st+=' '
    i+=n
print(st)
st=''
for i in range(0,len(s),len(s)//N):
    if len(s[i:i+len(s)//N:1])==len(s)//N:
        st+=s[i:i+len(s)//N:1]+' '
print(st)
'''





