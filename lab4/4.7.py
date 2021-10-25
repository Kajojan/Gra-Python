lista=[1111,100,1001,20,4,5,7]
maks=max(lista)
maks2=-999998
index=-1
for i in lista:
    index=index+1
    if i>maks:
        maks=i
    if i>maks2 and i<maks:
        maks2=i
        k = index
print(maks2,k)