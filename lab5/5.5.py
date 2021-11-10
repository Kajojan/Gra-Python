import random

y = 3
m = 3
lista = [[t for t in range(m)] for n in range (y) ]
for i in range(0, y):
    for j in range(0, m):
        x = random.randrange(100)
        lista[i][j] = x
for i in lista:
    print(i)
suma1=0
suma2=0
j=1
for i in range(0,y):
    suma1+=lista[i][i]
    suma2+=lista[i][m-j]
    j+=1
print("suma przekątnej zaczynając od lewej góry: ", suma1)
print("suma przekątnej zaczynając od prawej góry: ", suma2)

