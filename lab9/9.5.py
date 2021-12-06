d={'1':3, '2':3, "5":3, '6':5, '8':3}
def invert(d):
    d2={}
    for key in d.keys():
        lista = []
        for key2 in d.keys():
            if d[key] == d[key2]:
                lista.append(key2)
        print(lista)
        d2[d[key]]=lista
    return d2



print(invert(d))