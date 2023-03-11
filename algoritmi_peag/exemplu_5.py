# 5. Scrieți o funcție Python care generează o matrice cu 19 linii indivizi vectori binari de dimensiune
# 7, cu număr par de biți. Calitatea unui individ este dată de suma elementelor componente.
# Calculați și afișați indivizii cei mai buni (cu calitatea maximă).

import numpy as np

def fitness(x):
    if np.sum(x)%2==0:
       return np.sum(x)
    else: return 0

def generare(n):
    indivizi=np.zeros([n,8],dtype=int)
    for i in range(n):
        indivizi[i,:7]=np.random.uniform(0,2,7)
        indivizi[i,-1]=fitness(indivizi[i,:7])

    return indivizi

def evaluare(n=19):
    indivizi=generare(n)
    print(indivizi)
    maxim = np.max(indivizi[:, -1])
    print(maxim)

evaluare()