'''
#l=[[00,01,02],[10,11,12],[20,21,22]]
l=eval(input('list:'))
sum1=0
sum2=0
for i in range(len(l)):
    sum1+=l[i][i]
    sum2+=l[i][len(l[i])-i-1]
    

   
print(abs(sum1-sum2))
'''
'''
l=[4,2,5,6]
for i in range(max(l)):
    for j in range(len(l)):
        if i<l[j]:
            print("#",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#wpa to print how many lines of data present in a given file
#s='''HI \nHELLO \nI AM \nBASHEER '''
fo=open('data.txt','w')
s=['HI\n','HELLO\n','I AM\n','BASHEER\n','ANSARI\n']
fo.writelines(s)
fo.close()

'''
fo=open('data.txt','r')
var=fo.readlines()#var is a list containging every line as a element
print(len(var))
fo.close()
'''
'''
fo=open('data.txt','r')
var=fo.readlines()
sm=0
for i in range(len(var)):
    for j in range(len(var[i].split())):
        sm+=1
print(sm)
fo.close()
'''
'''
fo=open('data.txt','r')
var=fo.readlines()
sm=0
for i in var:
    for j in i:
        sm+=1
print(sm)
fo.close()
'''
'''
fo=open('data.txt','r')
var=fo.readlines()
for i in range(len(var)):
    a=var[i].split()
    for j in range(len(a)):
        if len(a[j])>5:
            print(a[j])
'''
'''
fo=open('data.txt','r')
var=fo.readlines()
for i in var:
    if len(i)>100:
        print(i)
'''
'''
fo=open('data.txt','r')
var=fo.readlines()
for i in var:
    for j in i.split():
        if j.startswith('ha'):
            print(j)
'''
'''
s=input()
s1=''
l=[]
for i in s:
    l.append(i)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i].isalpha() and l[j].isalpha():
            l[i],l[j]=l[j],l[i]


print(l)
for i in l:
    s1+=i
print(s1)
'''
l=eval(input("list"))
for i in range(len(l)):
    for j in range(1,len(l[i])+1):
        print(l[-j][i],end=' ')
    print()
