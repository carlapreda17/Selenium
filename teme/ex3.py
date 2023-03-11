
def bubble_sort(a):

    for linie in a:
        n=len(linie)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                 if linie[j] > linie[j+1]:
                    linie[j], linie[j + 1] = linie[j + 1], linie[j]
    print(a)


a = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]
bubble_sort(a)
