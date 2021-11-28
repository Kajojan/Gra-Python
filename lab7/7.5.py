def liczba(lista,x):
    n=0
    równe=-0
    mniejsze=0
    wieksze=0
    while n <len(lista):
        if lista[n]==x:
            równe+=1
        if lista[n]>x:
            wieksze+=1
        if lista[n]<x:
            mniejsze+=1
        n+=1
    return równe,wieksze, mniejsze

lista=[1,2,3,4,5,5,5,6,7,8,9]
print(liczba(lista,5))


