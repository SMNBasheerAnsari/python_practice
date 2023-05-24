print('finding max among 5 values')
a=int(input('enter 1st value:'))
b=int(input('enter 2nd value:'))
c=int(input('enter 3rd value:'))
d=int(input('enter 4th value:'))
e=int(input('enter 5th value:'))
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a,'a')
            else:
                print(e,'e1')
        else:
            if d>e:
                print(d,'d1')
            else:
                print(e,'e2')
    else:
        if c>d:
            if c>e:
                print(c,'c1')
            else:
                print(e,'e3')
        else:
            if d>e:
                print(d,'d2')
            else:
                print(e,'e4')
else:
    if b>c:
        if b>d:
            if b>e:
                print(b,'b')
            else:
                print(e,'e5')
        else:
            if d>e:
                print(d,'d3')
            else:
                print(e,'e6')
    else:
        if c>d:
            if c>e:
                print(c,'c2')
            else:
                print(e,'e7')
        else:
            if d>e:
                print(d,'d4')
            else:
                print(e,'e8')
            






















             
