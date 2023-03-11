import numpy as np

def minim(a):
    linii = len(a)
    coloane = len(a[0])
    vector_solutie=[]
    ok=1

    for j in range(coloane):
        min=a[0][j]
        for i in range(1,linii):
            if a[i][j] < min:
                min=a[i][j]
        if min==5:
            vector_solutie.append(j)

    print(vector_solutie)

a = [
    [89, 8, 9],
    [7, 6, 7],
    [8, 8, 5]
]
minim(a)
