fo=open('data.txt','w')
s=['HI\n','HELLO\n','I AM\n','BASHEER\n','ANSARI\n']
fo.writelines(s)
fo.close()


fo=open('data.txt','r')
var=fo.readlines()#var is a list containging every line as a element
print(len(var))
fo.close()

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
