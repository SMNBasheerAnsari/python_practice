'''
#passing & returning arg
def outer(arg):
    print('1st line of outer funtion')
    print(arg,'arg value')
    def inner():
        print('1st line of inner funtion')
        print(arg,'arg value in inner')
        print('last line in inner')
    inner()
    print('last line in outer')
    return arg
outer(23)
'''
'''
#passing arg & returning inner funtion address
def outer(arg):
    print('1st line of outer funtion')
    print(arg,'arg value')
    def inner():
        print()
        print('1st line of inner funtion')
        print(arg,'arg value in inner')
        print('last line in inner')
    inner()
    print()
    print('last line in outer')
    return inner
print(outer(23))
'''
'''
#returning inner funtion adress, calling internal funtion with name of veriable 
def outer(arg):
    print('1st line of outer funtion')
    print(arg,'arg value')
    def inner():
        print()
        print('1st line of inner funtion')
        print(arg,'arg value in inner')
        print('last line in inner')
    print()
    print('last line in outer')
    return inner
ver=outer(23)
ver()
'''
#returning internal funtion adress,calling second outer funtion inside innerfuntion space
def outer(arg):
    print('1st line of outer funtion')
    print(arg,'souter adress')
    def inner():
        print()
        print('1st line of inner funtion')
        arg()
        print()
        print('last line in inner')
        
    
    print('last line in outer')
    return inner
def souter():
    print('calling form inner funtion space')
    print('1st line in second outer funtion')
    print('0')
    print('1st line in second outer funtion')
ver=outer(souter)
ver()
