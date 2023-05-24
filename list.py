l=eval(input("enter a list:"))
n=int(input("enter a value:"))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if sum(l[i:j])==n:
            print(i+1,j)
        elif sum(l[i:j])>n:
            break
        
            
