import random
def random_lista(y):
    lista=[]
    for i in range(0,y):
        x = random.randrange(100)
        lista.append(x)
    return lista
lista1=random_lista(4)
lista2=random_lista(3)
print(lista1,lista2)
del lista1[len(lista1)-1]
for i in lista2:
    lista1.append(i)
print(lista1)
