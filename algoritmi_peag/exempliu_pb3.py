# 2. Scrieți o funcție Python care generează o matrice cu 8 linii vectori cu câte 6 biți. Calitatea unui
# individ (vector cu 6 biți) este dată de suma elementelor componente. Calculați și afișați
# a. individul cu cea mai mică valoare a funcției calitate – primul.
# b. Indivizii cu cea mai mică valoare a funcției calitate

import numpy as np

def fitness(x):
    return np.sum(x)

def generare(n):
    indivizi=np.zeros([n,7],dtype=float)
    for i in range(n):
        indivizi[i,:6]=np.random.uniform(0,2,6)
        indivizi[i,-1]=fitness(indivizi[i,:6])

    return indivizi

def pb_a(n=8):
    indivizi=generare(n)
    ind_min = np.argmin(indivizi[:, -1]) #returneaza indicele celui mai mic element
    return indivizi[ind_min, :6]

def pb_b(n=8):
    indivizi=generare(n)
    minim = np.min(indivizi[:, -1])
    # toate aparitiile valorii minime
    poz = np.where(indivizi[:, -1] == minim) #indivizii care au valoarea minima
    return indivizi[poz[0][:], :6]
