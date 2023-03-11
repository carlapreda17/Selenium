import numpy as np

def nr_linii(a):
    nr=0
    ok=0
    linii=len(a)
    coloane=len(a[0])
    for i in range(linii):
        for j in range(coloane-1):
                if a[i][j]>a[i][j+1]:
                        ok=1
        if ok==0:
             nr=nr+1
    print(nr)


a = [[1, 2, 3], [1, 2, 7], [5, 8, 9]]
nr_linii(a)

