def przes(lista,k):
    lista2=lista[-k:]+lista[:-k]
    return lista2
lista=[1,2,3,4,5,6,7]
print(przes(lista,3))
