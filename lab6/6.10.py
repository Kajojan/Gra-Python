def parzyste(lista):
    lista2=[]
    for i in lista:
        if i%2==0:
            lista2.append(i)
    return lista2
lista=[1,2,3,4,5,6,7,8,8]
print(parzyste(lista))