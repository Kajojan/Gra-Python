import random
y = 10
lista=[]
for i in range(0,y):
    x = random.randrange(15)
    lista.append(x)
print(lista)

element_szukany=5
for i in lista:
    if i == element_szukany:
        print("Tak")
        break
else:
    print("Nie")