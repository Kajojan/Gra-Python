import random
y = 3
m = 3
lista = [[t for t in range(m)] for n in range (y) ]
for i in range(0, y):
    for j in range(0, m):
        x = random.randrange(100)
        lista[i][j] = x
print(lista)
suma_max=0
suma_min=99999999999
for i in range (0,y):
    suma=0
    for j in lista[i]:
        suma+=j
    if suma > suma_max :
        suma_max=suma
        max=i
    if suma < suma_min:
        min=i
        suma_min=suma
print("najmniejsza suma: ",suma_min, " dla listy: ",lista[min])
print("najwieksza suma : ", suma_max,"dla listy: ",lista[max])