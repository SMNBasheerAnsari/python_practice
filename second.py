s=100
print(id(s))
print(type(s))
a=9.915
print(id(a))
print(type(a))
import keyword
keyword.kwlist
print(len(keyword.kwlist))
A=10
print(id(A))
B=20
print(id(B))
C=20
print(id(C))
D=40
print(id(D))
A=20
print(id(A))
print("s=",s,"a=",a,"keywodr-",keyword.kwlist,"A=",A,"B=",B, "C=",C, "D=",D, "A=",A)
s,a=a,s
print("s,a",s, a)

