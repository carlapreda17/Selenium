def inserare(a):
    for linie in a: #parcurgem fiecare linie
        n = len(linie)
        for i in range(1, n): #elementele de pe linia i

            x = linie[i]
            # Mutam elementele vectorului de la 0 la i-1 care sunt mai marti decat x
            j = i - 1
            while j >= 0 and x < linie[j]:
                linie[j + 1] = linie[j]
                j = j - 1
            linie[j + 1] = x
    print(a)


if __name__=='__main__':
    a=[
       [3, 2, 1],
       [6, 5, 4],
       [9, 8, 7]
      ]
    inserare(a)