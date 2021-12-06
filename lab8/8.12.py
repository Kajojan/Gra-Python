def tail(lista):
    del lista[0]
    return lista


def head(lista):
    if len(lista) > 0:
        return lista[0]


def reverse(lista):
    print(len(lista)-1)
    if len(lista) == 1:
        lista2[0]=head(lista)
        return lista2
    lista2[len(lista) - 1] = head(lista)
    return reverse(tail(lista))


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = []

print(reverse(lista))
