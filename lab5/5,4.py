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

print(lista)
index = m -1
for i in range(0, n):
    for j in range(0, m):
        print(lista[i][index]," ", end="")
        index-=1
    print("")

