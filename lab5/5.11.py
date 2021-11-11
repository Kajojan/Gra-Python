import random
y = 5
lista=[]
for i in range(0,y):
    x = random.randrange(100)
    lista.append(x)
print(lista)

max1=0
max2 = 0
for i in lista:
    if i >max1:
        max2=max1
        max1=i
    if i<max1 and i > max2:
        max2=i
print(max2)