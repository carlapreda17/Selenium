import numpy as np

def nr_linii(a):
    nr=0
    ok=0
    for row in a:
        if row==sorted(row):
            nr=nr+1
    print(nr)

if __name__=='__main__':
    a = [[5, 2, 3], [1, 2, 7], [5, 8, 9]]
    nr_linii(a)  #apelam functia

