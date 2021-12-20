planety=[{'nazwa':'Mars', 'gęstość':5.427 }, {'nazwa':"Ziemia", 'gęstość': 5.513}]
def dodanie(slownik,docelowy):
    docelowy.append(slownik)
    for i in range (len(docelowy)-1,0,-1):
        if docelowy[i]['nazwa'] < docelowy[i-1]['nazwa']:
            tmp=docelowy[i-1]
            docelowy[i-1]=docelowy[i]
            docelowy[i]=tmp
    return docelowy



slownik={'nazwa': "Wenus", 'gęstość': 5.204}
print(dodanie(slownik, planety))


def wartosci(p,tablica):
    for i in tablica:
        if i['nazwa']==p:
            return ( i['nazwa'] , i['gęstość'])
print(wartosci('Ziemia', planety))


def uppdate(nazwa,wartośc,lista):
    for i in lista:
        if i['nazwa']==nazwa:
            i['gęstość']=wartośc
            return lista

print(uppdate('Wenus', 5.501, planety))

def delet(lista,g):
    for i in range (0,len(lista)-1):
        if lista[i]['gęstość'] < g:
            del lista[i]

    return lista

print(delet(planety,5.500))

def indeks(lista, nazwa):
    pierw=0
    ostatni=len(lista)-1
    while pierw <=ostatni:
        s=(pierw+ostatni)//2
        if lista[s]["nazwa"]==nazwa:
            return s
        if lista[s]["nazwa"] > nazwa:
            ostatni=s-1
        if lista[s]["nazwa"] < nazwa:
            pierw=s+1
print(planety)
print(indeks(planety,'Ziemia'))


