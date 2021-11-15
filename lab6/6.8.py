def bezpowturzen(lista):
    lista2=[]

    lista2.append(lista[0])
    for i in lista:
        for j in lista2:
            powt = 0
            if j==i:
                powt+=1
        if powt==0:
            lista2.append(i)
    return lista2

lista=[1,1,2,3,4,4,4,4,5,5,6]
print(bezpowturzen(lista))

