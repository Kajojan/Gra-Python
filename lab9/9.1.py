def ispermutation(lista1,lista):
    ile=0
    for i in lista1:
        for j in lista:
            if j == i:
                ile+=1
    if ile >= len(lista1):
        return True
    else:
        return False

l1=[1,4,1,6,7]
l2=[4,7,1,6,1]
print(ispermutation(l1,l2))