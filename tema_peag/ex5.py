

def cmmdc(a,b):

    rest=a%b
    while rest!=0:
        a=b
        b=rest
        rest=a%b

    print(b)



if __name__=='__main__':
    cmmdc(5, 25)