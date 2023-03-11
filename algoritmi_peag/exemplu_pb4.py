# 3. Scieți o funcție Python care generează o matrice cu 10 linii permutări de dimensiune 8. Calitatea
# unui individ P(permutare de dimensiune 8) este dată de numărul perechilor (i,j), i<j, pentru care
# # P(i)>P(j). Evaluați cei 10 indivizi generați și afișați valoarea maximă.
import numpy as np


def fitness(x):
    nr_perechi=0
    for i in range(8):
        for j in range(i+1,8):
            if x[i]>x[j]:
                nr_perechi=nr_perechi+1
    return nr_perechi

def generare(n):
    indivizi=np.zeros([n,9],dtype=int)
    for i in range(n):
        indivizi[i,:8]=np.random.permutation(8)
        indivizi[i,-1]=fitness(indivizi[i,:8])

    return indivizi

def evaluare(n=10):
    indivizi=generare(n)
    print(indivizi)
    print(np.max(indivizi[:,-1])) #maximul dintre toate elementele aflate pe ultima coloana

