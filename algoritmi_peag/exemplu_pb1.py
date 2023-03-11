# 1. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{(𝑥, 𝑦, 𝑧)⁄𝑥, 𝑦, 𝑧 ∈ [−2,7]} → ℝ
# 𝑓(𝑥, 𝑦, 𝑧) = 𝑥
# 2 − 2𝑦 ∙ 𝑧
# Generați 10 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valorile obținute
# în ordine crescătoare

import numpy as np


def fitness(x): #functia calitate
 #return x[0]*x[0]-2*x[1]*x[2]
    return np.square(x[0])-2*x[1]*x[2]


def generare(n):
 indivizi=np.zeros([n,4],dtype="float") #matrice de 0
 # pe fiecare linie - primele 3 elemente(x,y,z)=individ, al 4-lea este valoarea f(x,y,z)
 for i in range(n):
    indivizi[i,:3]=np.random.uniform(-2,7,3) #ia 3 valori random din intervalul -2,7
    #indivizi[i,-1]= ultimul element din linia i calculeaza f(x,y,x)
    indivizi[i,-1]=fitness(indivizi[i,:3])
 return indivizi

def pb1(n=10):
 indivizi=generare(n)
 print(indivizi,"\n")
 indici=np.argsort(indivizi[:,-1]) #sorteaza crescator
 return indivizi[indici]
print(pb1())