def max(lista):
    n=0
    maks=0
    while n < len(lista):
        if lista[n]>maks:
            maks=lista[n]
        n+=1
    return maks

def sort_maks(lista):
    n=0
    lista2=lista
    while n < len(lista)-1:
        j=0
        while j < len(lista)-j-1:
            if lista[j]==max(lista):
                lista2[len(lista2) - j] = max(lista2[0:len(lista2) - j])
                tmp=lista2[len(lista2)-j]
                lista2[j]=tmp
                print(max(lista), lista[j])
            j+=1
        n+=1

    return lista2

lista=[2,3,4,1,8,9,5]
print(sort_maks(lista))
print(max(lista))

