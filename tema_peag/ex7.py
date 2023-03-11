def inserare_vector(arr):

    for i in range(1, len(arr)):

        x = arr[i]
        #Mutam elementele vectorului de la 0 la i-1 care sunt mai marti decat x
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j=j- 1
        arr[j + 1] = x
    print(arr)


if __name__=='__main__':
    arr = [66, 151, 13, 2, 9]
    inserare_vector(arr)