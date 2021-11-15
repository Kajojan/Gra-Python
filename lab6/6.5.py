def rewers(a):
    napis = ""
    i=len(a)-1
    #for j in a:
    while(i>=0):#for i in range (len(a)-1,-1,-1)
        napis=napis+a[i]
        i=i-1
    return napis

napis="1234"
print(rewers(napis))



