import numpy as np

def permutare_identica(perm):
    permutare_id = np.arange(1, len(perm) + 1)
    print(np.array_equal(perm, permutare_id))

if __name__=='__main__':
    perm=[1,2,4,5]
    permutare_identica(perm)
