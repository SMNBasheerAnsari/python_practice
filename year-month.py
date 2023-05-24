y=int(input())
m=int(input())
l1=[1,3,5,7,8,10,12]
l2=[4,6,9,11]
if m in l1:
    print("31 days in given month")
elif m in l2:
    print("30 days in given month")
elif m==2:
    if (y%400==0) or (y%4==0 and y%100!=0):
        print("29 days in given month")
    else:
        print("28 days in given month")
else:
    print(" enterd month is invalid") 
