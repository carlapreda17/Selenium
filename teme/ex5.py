

def cmmdc(a,b):

    rest=a%b
    while rest!=0:
        a=b
        b=rest
        rest=a%b

    print(b)

cmmdc(5,25)

