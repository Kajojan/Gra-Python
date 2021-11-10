import random
y = 3
m = 3
k=2
lista = [[t for t in range(m)] for n in range (y) ]
for i in range(0, y):
    for j in range(0, 2):
        x = random.randrange(100)
        lista[i][j] = x
for i in lista:
    print(i)
print("mnożnik: ",k)
for i in range(0, y):
    for j in range(0, m):
        lista[i][j]*=k
for i in lista:
    print(i)