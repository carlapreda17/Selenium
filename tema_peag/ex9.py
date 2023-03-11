import numpy as np



def generare(n,m):

    vector=[]
    matrice=[]

    for i in range(n): #populam matricea cu numere random
        suma=0
        row=np.random.uniform(0,1000,n)
        matrice.append(row)
        calitate=sum(row)
        vector.append(calitate)


    print(vector)
    print(matrice)

if __name__=='__main__':
    generare(7,20)