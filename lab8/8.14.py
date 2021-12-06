def tail(lista):
    del lista[0]
    return lista

def head(lista):
    if len(lista)>0:
        return lista[0]

def is_sorted(lista):
    if head(lista) < head(tail(lista)):
        if len(lista)==2:
            return True
        return is_sorted(tail(lista))
    else:
        return False


lista=[1,2,3,4,5,3]
print(is_sorted(lista))



