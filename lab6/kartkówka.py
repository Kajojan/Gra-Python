lista=[[1,2,3],[1,2,3],[1,2,3]]
j=2
for i in range(0,3):
    L=lista[i]
    if i%2==0 or i==0:
        print(L[i])
    else:
        print(L[j-i])
        j=j-1