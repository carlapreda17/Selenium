def inserare(matrice):
    linii=len(a)
    coloane=len(a[0])
    for j in range(coloane):
        for i in range(linii):
            x = a[i][j]
            k = i - 1
            while k >= 0 and a[k][j] > x:
                a[k+1][j] = a[k][j]
                k -= 1
            a[k+1][j] = x
    print(a)

a= [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]
inserare(a)