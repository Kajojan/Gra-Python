def tail(lista):
    del lista[0]
    return lista

def head(lista):
    if len(lista)>0:
        return lista[0]
lista4=[]
def together(lista1,lista2):
    if len(lista1)==0 and len(lista2)==0:
        return lista4
    if len(lista1)==0:
        lista4.append(head(lista2))
        return together(lista1, tail(lista2))

    if len(lista2)==0:
        lista4.append(head(lista1))
        return together(tail(lista1),lista2)

    if head(lista1)<head(lista2):
        lista4.append(head(lista1))
        return together(tail(lista1),lista2)
    else:
        lista4.append(head(lista2))
        return together(lista1, tail(lista2))

lista=[1,2,3,4,5,6,6]
lista2=[1,1,1,4,4,7,7,9]
print(together(lista,lista2))
