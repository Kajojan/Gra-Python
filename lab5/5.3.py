import random
def randomlista(x):
    lista=[]
    l=0
    for i in range(0,x):
        x = random.randrange(l,100)
        l=x
        lista.append(x)
    return lista
lista1=randomlista(3)
lista2=randomlista(3)
dl=len(lista2)+len(lista1)
print(lista1)
print(lista2)
k=0
j=0
lista3=[]
for i in range (0,dl):
    if k<len(lista1):
        if lista1[k]<lista2[j]:
            lista3.append(lista1[k])
            if k<len(lista1)-1:
                k = k + 1
    elif j<len(lista2):
        if lista1[k]>=lista2[j]:
            lista3.append(lista2[j])
            if j<len(lista2)-1:
                j= j + 1
    elif k == len(lista1) - 1:
        lista3.append(lista2[j])
        j = j + 1

    elif j == len(lista2) - 1:
        lista3.append(lista1[k])
        k = k + 1



print(lista3)



