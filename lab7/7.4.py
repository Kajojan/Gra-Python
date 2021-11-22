def ostatni(lista,x):
    pierw=0
    ostat= len(lista)-1
    ostatni=-1
    while pierw<=ostat:
        s=(pierw+ostat)//2
        if lista[s] == x:
            ostatni=lista[s]
            while i <
                ostatni=lista[s+1]
            return ostatni
        if lista[s] > x:
            ostatni = s - 1
        else:
            pierw=s+1




lista=[1,2,3,4,4,4,5,6,7]
print(ostatni(lista,4))