import numpy as np

def minim(a):
    linii = len(a)
    coloane = len(a[0])
    vector_solutie=[]
    ok=1

    for j in range(coloane):
        min=99999 #la fiecare coloana luam un minim cu care sa comparam elementele
        for i in range(linii):
            if a[i][j] < min:
                min=a[i][j]
        if min==5:
            vector_solutie.append(j)

    print(vector_solutie)
if __name__=='__main__':
    a = [
         [7, 8, 9],
         [8, 5, 7],
         [6, 8, 5]
        ]
    minim(a)
