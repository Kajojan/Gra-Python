def sort(lista):
    s=0
    for i in range(0,len(lista)-1):
        if lista[i]<lista[i+1]:
            s+=1
    if s==len(lista)-1:
        return True
    else:
        return False


lista=[1,2,3,4,5,10]
print(sort(lista))