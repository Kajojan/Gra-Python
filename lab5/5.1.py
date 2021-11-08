import random
y = random.randrange(10)
lista=[]
for i in range(0,y):
    x = random.randrange(100)
    lista.append(x)
print(lista)
index=0
for i in lista:
    if index%2==0:
        print(i)
    index+=1

