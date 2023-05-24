Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i=int(10+5j)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    i=int(10+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
f=float(10+5j)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    f=float(10+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
c=complex(4)
c
(4+0j)
s='4+5j'
int(s)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '4+5j'
float(s)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: '4+5j'
complex(s)
(4+5j)
s='string to split'
s.split()
['string', 'to', 'split']
s.split('i')
['str', 'ng to spl', 't']
s.rsplit('i')
['str', 'ng to spl', 't']
s.rsplit()
['string', 'to', 'split']
s.replace('tr','t')
'sting to split'
t='taatoos'
len(t)
7
t.replace('aa','A')
'tAtoos'
t.replace('oo','U')
'taatUs'
len(t)
7
p='python'
len(p)
6
p.endswith('on')
True
p.endswith('on',6)
False
p.endswith('on',4)
True
p.endswith('on',,6)
SyntaxError: invalid syntax
p.endswith('on',5,10)
False
p.endswith('on',4,7)
True
' '.join([29,'k','o'])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    ' '.join([29,'k','o'])
TypeError: sequence item 0: expected str instance, int found
' '.join('str')
's t r'
s='index'
s.index('ex')
3
s.index('xe)
        
SyntaxError: incomplete input
s.index('xe')
        
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.index('xe')
ValueError: substring not found
s.rindex('xe')
        
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.rindex('xe')
ValueError: substring not found
s.rindex('ex')
        
3
s.find('x')
        
4
s.find('z')
        
-1
s.rfind('z')
        
-1
s.find('x')
        
4
s.rfind('x')
        
4
s.strip()
        
'index'
s={2,4,6,8,10}
        
s.add(1)
        
s
        
{1, 2, 4, 6, 8, 10}
s.add(3)
        
s
        
{1, 2, 3, 4, 6, 8, 10}
s.add(11)
        
s
        
{1, 2, 3, 4, 6, 8, 10, 11}
s.add(55)
        
s
        
{1, 2, 3, 4, 6, 8, 10, 11, 55}
s.add(-6)
        
s
        
{1, 2, 3, 4, 6, 8, 10, 11, 55, -6}
s.add(True)
        
s
        
{1, 2, 3, 4, 6, 8, 10, 11, 55, -6}
s=
        
SyntaxError: incomplete input
s={True,3,6,8,10}
        
s
        
{True, 3, 6, 8, 10}
s.add(1)
        
s
        
{True, 3, 6, 8, 10}
s.add(False)
        
s
        
{False, True, 3, 6, 8, 10}
s.add(0)
        
s
        
{False, True, 3, 6, 8, 10}
d={'n':'basheer','a':23}
        
d.pop('a')
        
23
{4,5}+{6,7}
        
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    {4,5}+{6,7}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
not 7
        
False
>>> not[]
...         
True
>>> 2 in 123
...         
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    2 in 123
TypeError: argument of type 'int' is not iterable
>>> 2 in '123'
...         
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    2 in '123'
TypeError: 'in <string>' requires string as left operand, not int
>>> 3 in [3,4,5]
...         
True
>>> print(10,20,30,40,50,sep=',',end='')
...         
10,20,30,40,50
>>> print(10,20,30,40,50,sep=',',end=' ')
...         
10,20,30,40,50 
>>> print(10,20,30,40,50,sep=,,end='')
...         
SyntaxError: invalid syntax
>>> print(10,20,30,40,50,sep=' ',end=',')
...         
10 20 30 40 50,
print(44)
