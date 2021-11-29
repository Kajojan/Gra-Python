def czy(x,lista):
    s=lista[(len(lista)-1)//2]
    if s==x:
        return True
    elif s<x:
        return czy(x,lista[(len(lista))//2:(len(lista))])
    elif s>x:
        return czy(x,lista[0:(len(lista))//2])

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(czy(15,lista))