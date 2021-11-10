import random
n= 2
m= 3
lista = [[t for t in range(m)] for k in range (n) ]
for i in range(0, n):
    for j in range(0, m):
        x = random.randrange(100)
        lista[i][j] = x
print(lista)
index = m -1
for i in range(0, n):
    for j in range(0, m):
        print(lista[i][index]," ", end="")
        index-=1
    print("")

