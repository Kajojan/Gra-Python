def czy_jest(lista,n):
    for i in lista:
        if i == n:
            return True
    else:
        return False
lista=["1","2"]
print(czy_jest(lista,"1"))