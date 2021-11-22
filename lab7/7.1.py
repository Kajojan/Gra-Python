import random
def lista(n):
    lista1=[]
    i=0
    while i < n:
        x=random.randint(-100,100)
        lista1.append(x)
        i+=1
    return lista1

print(lista(10))
