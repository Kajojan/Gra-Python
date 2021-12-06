def ostatni(lista,x):
    pierw=0
    ostat= len(lista)-1
    ostatni=-1
    while pierw<=ostat:
        s=(pierw+ostat)//2
        if lista[s] == x:
            ostatni=s
            i=1
            while lista[s+i]==x:
                ostatni=s+i
                i+=1
            return ostatni
        else:
            if lista[s] > x:
                ostatni = s - 1
            else:
                pierw=s+1
    return False





lista=[1,2,3,4,4,4,4,5,6,7,7,7,7,8]
print(ostatni(lista,7))