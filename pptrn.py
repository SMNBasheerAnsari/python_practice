number=int(input())
star=number
space=0
for i in range(number):
    for s in range(space):
        print(' ',end=' ')
    for m in range(star):
        print('*',end=' ')
    space+=1
    star-=1
    print()
