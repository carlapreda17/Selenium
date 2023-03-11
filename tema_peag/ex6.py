import numpy as np

def transpusa(A):
    print(np.transpose(A))


def produs(A, B):
    print(np.dot(A, B))


def suma(A, B):
    print(np.add(A, B))

def putere_matrce(A, n):
    print(np.linalg.matrix_power(A, n))
if __name__=='__main__':
    A=[
       [3, 2, 1],
       [6, 5, 4],
       [9, 8, 7]
      ]
    B=[
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]
      ]
    n=3
    transpusa(A)
    produs(A,B)
    suma(A,B)
    putere_matrce(A,n)