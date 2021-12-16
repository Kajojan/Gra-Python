def max(lista):
    n=0
    maks=0
    while n < len(lista):
        if lista[n]>maks:
            maks=lista[n]
        n+=1
    return maks

def sort_maks(lista):
    lista2=lista

    k=0
    n=0
    while n < len(lista):
        j=0
        while j < len(lista):
            lista2=lista[0:len(lista)-k]

            if lista[j]==max(lista2):
                tmp = lista[len(lista) - 1-k]
                lista[len(lista)-1-k] = max(lista2)
                lista[j]=tmp

                k+=1
            j+=1
        n+=1
    return lista

def test_sort_maks():
    lista = [2, 3, 3, 9, 4, 1, 8, 9, 5]
    assert sort_maks(lista) ==sorted(lista)
    


