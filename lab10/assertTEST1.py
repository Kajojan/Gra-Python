def wyszukaj(lista,x):
    pierwszy=0
    ostatni=len(lista)-1
    while (pierwszy <= ostatni):
        s=(pierwszy+ostatni)//2
        if lista[s] == x:
            return True
        if lista[s] > x:
            ostatni = s - 1
        else:
            pierwszy = s + 1
    else:
        return False

def test_spr():
    lista=[1,2,3,4,5,6,7,8]
    x=1
    assert wyszukaj(lista,x)==(x in lista)
    x=0
    assert wyszukaj(lista, x) == (x in lista)
    x=10
    assert wyszukaj(lista, x) == (x in lista)
    for x in [1,5,9]:
        assert wyszukaj(lista, x) == (x in lista)
