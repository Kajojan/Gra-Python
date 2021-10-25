lista=[-1111,100,1001,200000,4,5,7]
mini=999999
index=-1
for i in lista:
    index=index+1
    if i<mini:
        mini=i
        k=index
print(mini,k )