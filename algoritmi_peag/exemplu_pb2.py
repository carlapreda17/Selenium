# 4. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{(𝑥, 𝑦, 𝑧, 𝑢,𝑡)⁄𝑥, 𝑦, 𝑧 ∈ [−2,7], 𝑢,𝑡 ∈ {0,1}} → ℝ
# 𝑓(𝑥, 𝑦, 𝑧, 𝑢,𝑡) = 𝑢 ∙ 𝑥
# 2 − 𝑡 ∙ 𝑦 ∙ 𝑧
# Generați 12 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valoarea
#  medie
import numpy as np

def fintess(x): #functia calitate returneaza f(x,y,z,u,t)

    return  x[3]*np.square(x[0])-x[1]*x[2]*x[4]

def generare(n):
    indivizi=np.zeros([n,6],dtype=float)
    for i in range(n):
        indivizi[i,:3]=np.random.uniform(-2,7,3) #x,y,z interval din enunt
        indivizi[i,3:5]=np.random.uniform(0,2,2)  #u,t
        indivizi[i,-1]=fintess(indivizi[i,:5])
    return indivizi

def media_solutiilor(n=12):
    indivizi=generare(n)
    media=np.mean(indivizi[:,-1])
    print(media)

media_solutiilor()