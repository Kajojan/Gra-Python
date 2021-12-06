def tail(lista):
    del lista[0]
    return lista

lista=[1]


def is_empty(lista):
    lista=tail(lista)
    if len(lista)==0:
        return True
    else:
        return False

print(is_empty(lista))