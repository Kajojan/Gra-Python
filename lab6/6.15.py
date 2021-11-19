def zamian(lista,a,b):
    lista2=lista
    liczba=lista[a]
    lista2[a]=lista[b]
    lista2[b]=liczba
    return lista2
lista=[1,2,3,4,5,6]
print(zamian(lista,1,5))
