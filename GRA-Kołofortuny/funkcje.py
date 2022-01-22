import random
import time
import datetime
import csv
import sys

samogłoski=['b', 'c', 'ć', 'd', 'f','h', 'g', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż']
spółgłoski=['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó']
alfabet=['b', 'c', 'ć', 'd', 'f','h', 'g', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż','a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó']

def kolo():
    kolo1={1:100, 2:200, 3:250, 4:400, 5:500, 6:550, 7:1000, 8:"500?", 9:"Nagroda", 10:"BANKRUT!!!", 11:3000, 12:800, 13:50, 14:100, 15:200, 16:100, 17:200, 18:1000, 19:100, 20:2000}
    x = random.randrange(1,21)
    for i in kolo1.keys():
        if i == x:
            return kolo1[i]

def znacznik():
    znacznik=[]
    for i in range(0,3):
        znacznik.append(kolo())
    return znacznik

def losowanie():
    kategorie=["Znani Polscy Aktorzy", "Filmy", "Seriale", "Polskie przysłowia", "Państwa"]
    x = random.choice(kategorie)
    return x

def haslo(x):
    with open('kategorie.csv', encoding='utf-8') as csvfile:
        kategorie = csv.reader(csvfile, delimiter=';')
        for row in kategorie:
            if row[0] == x:
                k = random.randrange(1,91)
                haslo=row[k]
                return(haslo)

def nagrody():
    nagro={1:"Garnki kuchenne", 2:"Wyjazd na Mazury", 3:"Zestaw porcelany", 4:"Zestaw zegarków", 5:"Wyjazd na Malediwy", 6:"Piątke od prowadzącego"}
    x = random.randrange(1,7)
    for i in nagro.keys():
        if i == x:
            return nagro[i]

def odslanianie():
    x=random.randrange(1,3)
    if x==1:
        return 3500
    else:
        return "BANKRUT!!!"

def odgadywanie(has):
    odp=[]
    for i in has:
        odp.append(i)
    for i in range(len(has)):
        for j in alfabet:
            if odp[i]==j:
                odp[i]=" _ "
            elif odp[i]==" ":
                odp[i]="    "
    return odp

def kasowanie(nagroda,wynik,kasa):
    ile=0
    if nagroda != "BANKRUT!!!":
        for i in range(0,len(wynik)):
            if wynik[i] !=" _ ":
                ile+=1
            if ile != 0:
                kasa=kasa+(ile*nagroda)
    return kasa

def krecenie(życia):
    nagroda = kolo()
    print("wylosowałeś: ", nagroda)

    nagroda=ngro(nagroda,życia)
    return nagroda

def ngro(nagroda,życia):
    if nagroda == "BANKRUT!!!":
        życia -= 1
        print("Na szczęście nie jest to prawdziwe koło fortuny i nie tracisz całej kasy tylko tracisz 1 życie zostało ci ",życia)

    elif nagroda == "Nagroda":
        n = nagrody()
        print("Jeśli zgadniesz litera dostaniesz: ", n)
        nagroda=0
    elif nagroda == "500?":
        print("masz dwie opcje: 1.zostajesz przy 500  czy 2.odsłaniasz karte i ryzykujesz 50/50 3500 albo bankrut")
        wybor = input("1 czy 2 ?")
        if wybor == "1":
            nagroda = 500
            print("Wybrełeś 500")
        elif wybor == "2":
            druga = odslanianie()
            print("Po drugiej strona jest...", druga)
            nagroda=druga
    return nagroda

def czy_sp(litera):
    for i in samogłoski:
        if i == litera:
            return True

def czy_sa(litera):
    for i in spółgłoski:
        if i == litera:
            return True


def finalowe():
    nagrod={1:10000, 2:20000, 3:5000, 4:"Samochód", 5:1000, 6:3000, 7:2500, 8:1500}
    x = random.randrange(1, 9)
    for i in nagrod.keys():
        if i == x:
            return nagrod[i]

def bankrut(nagroda,życia,kasa,has):
    while nagroda=="BANKRUT!!!":
        życia = życia - 1
        życia2(życia,kasa,has)
        print("Wylosowałeś bankruta, zostalo ci", życia,"żyć ")
        k = input("Zakreć kołem jeszcze raz: ")
        kolo2(k)
        nagroda = krecenie(życia)
    return nagroda

def kolo2(k):
    while k != "kolo":
        k = input("Napisałeś źle kolo")

def życia2(życia,kasa, has):
    if życia == 0 :
        print("Pzegrałeś, skończyły ci się życia - wygraleś: ",kasa)
        print("Hasło to : ",has)
        sys.exit(0)

def odgadywaniehasła(kasa,has,wynik,życia,nagroda):
    sp = 0
    sp2 = 0
    for i in has:
        for j in samogłoski:
            if i == j:
                sp += 1
    while sp !=sp2:
        ile=0
        litera=input("Podaj spółgłoskę")
        for j in samogłoski:
            if j == litera:
                for i in range(0, len(has)):
                    if litera == wynik[i]:
                        break
                    if has[i] == litera:
                        wynik[i] = litera
                        sp2+=1
                        ile+=1
                if ile !=0:

                    kasa += ile * nagroda
                if ile !=0 and sp !=sp2:
                    print("Brawo Zgadłeś zgarnałeś: ", ile*nagroda,  "  aktualny stan twojej wygranej: ", kasa)
                    print(wynik)
                    k = input("Napisz 'kolo' aby zakręcisz kołem")
                    kolo2(k)
                    nagroda=krecenie(życia)
                    bankrut(nagroda, życia,kasa,has)
                    nagroda=bankrut(nagroda,życia,kasa,has)
                if ile==0 and sp !=sp2:
                    życia-=1
                    życia2(życia,kasa,has)
                    print("Nie ma takiej literki lub już ją podałeś, tracisz jedno życie zostało ci: ",życia, " zakreć kołem jeszcze raz, aby grać dalej")

                    print(wynik)
                    k = input("Napisz 'kolo' aby zakręcisz kołem")
                    kolo2(k)
                    nagroda = krecenie(życia)
                    nagroda=bankrut(nagroda, życia,kasa,has)
        else:
            print("Prosze o podanie spółgłoski")
            print(wynik)
    return kasa, życia






def czas():
    global s
    s=90
    while s > 0:
        if s == 45:
            print("---Połowa czasu mineła---")
        time.sleep(1)
        s-= 1
    print("Czas się skończył, prosze naciśnij Enter")



