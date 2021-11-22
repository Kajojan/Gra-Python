def sprawdz(lista,a):
    pierw=0
    ostat=len(lista)-1
    while pierw <= ostat:
        s=(pierw+ostat)//2
        if lista[s]== a:
            return True
        if lista[s]>a:
            ostat = s -1
        else:
            pierw = s +1
    return False

lista=[1,2,3,4,5,6,7,8,9,10]
print(sprawdz(lista,5))




