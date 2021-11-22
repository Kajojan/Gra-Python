def ostatni(lista,x):
    ostatni=-1
    index=0
    while index<len(lista):
        if lista[index]==x:
            ostatni=index
        index+=1
    return ostatni


lista=[1,2,3,4,5,6,7,3,9]
print(ostatni(lista,3))