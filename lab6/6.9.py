def czy_pierwsza(a):
    licznik=0
    for i in range(1,a+1):
        if a%i==0:
            licznik+=1
    if licznik==2:
        return True
    else:
        return False
print(czy_pierwsza(10))