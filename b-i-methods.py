Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=str()
s.lower()
''
l=list()
l.lower()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l.lower()
AttributeError: 'list' object has no attribute 'lower'
s.islower()
False
s='1abcd'
s.islower()
True
s='1ABCD'
s.isupper()
True
s='abcd123@#$."'
s.islower()
True
s='abcd123@#$."A'
s.islower()
False
s.lower()
'abcd123@#$."a'
s.isupper()
False
s.upper()
'ABCD123@#$."A'
s=s.upper()
s.isupper()
True
u=str()
u.upper()
''
s='ABCD123@#$."a'
s.isupper()
False
u.isuper()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    u.isuper()
AttributeError: 'str' object has no attribute 'isuper'. Did you mean: 'isupper'?
u.isupper()
False
s.title()
'Abcd123@#$."A'
s='asdf jkl;gh'
s.title()
'Asdf Jkl;Gh'
s.istitle()
False
s.isalpha()
False
s='Abcd 1234 @#$ .";/ aBCD'
s.capitalize()
'Abcd 1234 @#$ .";/ abcd'
s.swapcase()
'aBCD 1234 @#$ .";/ Abcd'
s.lower()
'abcd 1234 @#$ .";/ abcd'
s.upper()
'ABCD 1234 @#$ .";/ ABCD'
s.title()
'Abcd 1234 @#$ .";/ Abcd'
s.islower()
False
s.isupper()
False
s.istitle()
False
s.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
s.isalpha()
False
s.isdigit()
False
s.isalnum()
False
s.isspace()
False
e=''
e.lower()
''
e.upper()
''
e.title()
''
e.capitalize()
''
e.swapcase()
''
e.islower()
False
e.isupper()
False
e.istitle()
False
e.isdigit()
False
e.isalpha()
False
e.isalnum()
False
e.isspace()
False
s.split()
['Abcd', '1234', '@#$', '.";/', 'aBCD']
s.rsplit()
['Abcd', '1234', '@#$', '.";/', 'aBCD']
s.split(,-1)
SyntaxError: invalid syntax
s.split(' ',-1)
['Abcd', '1234', '@#$', '.";/', 'aBCD']
s.split('',0)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.split('',0)
ValueError: empty separator
s.split(" ",0)
['Abcd 1234 @#$ .";/ aBCD']
string='STRING TO SPLIT'
string.split(' ',0)
['STRING TO SPLIT']
sting.rsplit('z')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sting.rsplit('z')
NameError: name 'sting' is not defined. Did you mean: 'string'?
string.split('z')
['STRING TO SPLIT']
string.rsplit('x')
['STRING TO SPLIT']
string.replace('S','s',count=-1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    string.replace('S','s',count=-1)
TypeError: str.replace() takes no keyword arguments
string.replace('S','s')
'sTRING TO sPLIT'
string.replace()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    string.replace()
TypeError: replace expected at least 2 arguments, got 0
string.replace('SPLIT','REPLACE')
'STRING TO REPLACE'
s.startswith('A')
True
s.endswith('D')
True
s.endswith('d')
False
s.startswith('A',0,100)
True
s.endswith('D',22)
True
s.endswith('D',22,0)
False
s.endswith('D',0,22)
False
s.endswith('D',0,23)
True
s.endswith('D',0,24)
True
s.endswith('D',25)
False
s.startswith('A',25)
False
s.starswith('A',24)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s.starswith('A',24)
AttributeError: 'str' object has no attribute 'starswith'. Did you mean: 'startswith'?
s
'Abcd 1234 @#$ .";/ aBCD'
s.startswith('A',23)
False
s.startswith('A',0)
True
s=string
s
'STRING TO SPLIT'
s.coutn('S')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    s.coutn('S')
AttributeError: 'str' object has no attribute 'coutn'. Did you mean: 'count'?
s.count('S')
2
s.count('s')
0
s.index('S')
0
s.index('S',10)
10
s.index('I',6)
13
s.rindex('I',6)
13
s.count('S',9)
1
s.rindex('I',-2)
13
s.rindex('T',-2)
14
len(s)
15
s.index('T',13)
14
s.rindex('T',9,2)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    s.rindex('T',9,2)
ValueError: substring not found
s.rindex('T',0,9)
7
s.rindex('T',4,15)
14
s.find('S',0,15)
0
s.find('S',2,15)
10
s.rfind('S',0,15)
10
s.rfind('S',0,9)
0
s.find('z',0)
-1
s.index('z',0)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    s.index('z',0)
ValueError: substring not found
e.split()
[]
e.rsplit()
[]
s
'STRING TO SPLIT'
s.split()
['STRING', 'TO', 'SPLIT']
s.rsplit()
['STRING', 'TO', 'SPLIT']
s.split(' ',2)
['STRING', 'TO', 'SPLIT']
s.rsplit(' ',2)
['STRING', 'TO', 'SPLIT']
s.split(' ',1)
['STRING', 'TO SPLIT']
s.rsplit(' ',1)
['STRING TO', 'SPLIT']
s
'STRING TO SPLIT'
s.index('S',0)
0
s.rindex('S')
10
s.rindex('S',0)
10
s.rindex('S',11)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    s.rindex('S',11)
ValueError: substring not found
s='STRINGTOSPLIT'
s.index('S',1,10)
8
s.index('S',1)
8
s.rindex('S')
8
s.index('S',0,13)
0
s.rindex('S',0,13)
8
s.rindex('s',-1,-14)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    s.rindex('s',-1,-14)
ValueError: substring not found
s.rindex('S',-1,-14)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    s.rindex('S',-1,-14)
ValueError: substring not found
s.rindex('S',-14,-1)
8
s.index('S',-14,-1)
0
s.rindex('S',0)
8
s.rindex('S',1,10)
8
s.rindex('S',1)
8
' '.joint('string')
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    ' '.joint('string')
AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?
' '.join('string')
's t r i n g'
l=[]
' '.join(l)
''
l=[2,3,4,5,,6]
SyntaxError: invalid syntax
l=[2,3,4,5,6]
','.join(l)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    ','.join(l)
TypeError: sequence item 0: expected str instance, int found
>>> l=[1,2,3,4,5,6,7,8,9,10]
>>> l.count(1)
1
>>> l.count(30)
0
>>> l.count(4)
1
>>> l.index(30)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    l.index(30)
ValueError: 30 is not in list
>>> l.sort()
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l=[3,4,5,2,5,8,9]
>>> l.sort()
>>> l
[2, 3, 4, 5, 5, 8, 9]
>>> t=(2,3,4,6,8,90)
>>> t.count(4)
1
>>> t.index(4)
2
>>> t.index(5)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    t.index(5)
ValueError: tuple.index(x): x not in tuple
