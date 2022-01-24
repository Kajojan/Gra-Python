import sys

from funkcje import *
def test_czy_sp():
    a="a"
    b="b"
    assert czy_sp(a)==None
    assert czy_sp(b)==True
def test_czy_sa():
    a = "a"
    b = "b"
    assert czy_sa(a) == True
    assert czy_sa(b) == None

def test_sort():
    lista=[{'miejsce':1,'imie':"Kajo", 'wynik':120}, {'miejsce':1,'imie':"Kajo2", 'wynik':220}]
    assert sort(lista)==[{'miejsce':1,'imie':"Kajo2", 'wynik':220},{'miejsce':1,'imie':"Kajo", 'wynik':120}]

def test_od():
    k=odslanianie()
    assert k=="BANKRUT!!!" or k==1300

def test_kat():
    k=losowanie()
    assert k=="Znani Polscy Aktorzy" or k=="Filmy" or k =="Seriale" or k=="Państwa" or k=="Polskie przysłowia"