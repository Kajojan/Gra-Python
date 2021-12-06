def liczba(lista,x):
    n = 0
    równe = -0
    mniejsze = 0
    wieksze = 0
    pierw = 0
    ostat = len(lista) - 1
    ostatni = -1
    while pierw<=ostat:
        s=(pierw+ostat)//2
        if lista[s]==x:
            równe+=1
            ostatni=s
            i=1
            while lista[s+i]==x:
                równe+=1
                ostatni=s+i
                i+=1
            j=1
            while lista[s - j] == x:
                równe += 1
                j += 1
            wieksze=len(lista)-1-ostatni
            mniejsze=len(lista)-równe-wieksze
            return równe,wieksze,mniejsze
        if lista[s]<x:
            pierw=s+1
        if lista[s]>x:
            ostat=s-1

lista=[1,2,3,7,8,9,10,11]
print(liczba(lista,11))