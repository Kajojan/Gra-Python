def tail(lista):
    del lista[0]
    return lista

def head(lista):
    if len(lista)>0:
        return lista[0]

def czy_jest(lista,x):
    if head(lista)==x:
        return True
    if len(lista)==0:
        return False
    return czy_jest(tail(lista),x)

lista=[1,2,3,4,5,6]
print(czy_jest(lista,7))
