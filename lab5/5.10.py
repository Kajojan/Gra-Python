import random
n= 2
m= 3
lista = []
for i in range(0, n):
    lista2 = []
    lista.append(lista2)
    for j in range(0, m):
        x = random.randrange(100)
        lista2.append(x)

for i in lista:
    print(i)

lista3 = []
for i in range(0, m):
    lista4 = []
    lista3.append(lista4)
    for j in range(0, n):
        x=lista[j][i]
        lista4.append(x)


for i in lista3:
    print(i)

