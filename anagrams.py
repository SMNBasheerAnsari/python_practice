a=input('enter first string')
b=input('enter second string')
if sorted(a)==sorted(b):
    print('given strings are anagrams')
else:
    print('given strings are not anagrams')


c=int(input('enter a year'))
if c%4==0 and c%400==0:
    print('given year is leap year')
else:
    print('given year is not a leap year')
