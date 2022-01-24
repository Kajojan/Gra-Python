import random
import time
import datetime
import csv
import sys
import threading
samogłoski=['b', 'c', 'ć', 'd', 'f','h', 'g', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż']
spółgłoski=['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó']
alfabet=['b', 'c', 'ć', 'd', 'f','h', 'g', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż','a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó']

def kolo():
    kolo1={1:100, 2:200, 3:200, 4:150, 5:300, 6:50, 7:10, 8:"500?", 9:"Nagroda", 10:"BANKRUT!!!", 11:100, 12:"BANKRUT!!!", 13:1200, 14:100, 15:200, 16:100, 17:200, 18:1000, 19:100, 20:400}
    x = random.randrange(1,21)
    for i in kolo1.keys():
        if i == x:
            return kolo1[i]



def losowanie():
    kategorie=("Znani Polscy Aktorzy", "Filmy", "Seriale", "Polskie przysłowia", "Państwa")
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
        return 1300
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

    nagroda2=ngro(nagroda,życia)
    return nagroda2



def ngro(nagroda,życia):
    if nagroda == "BANKRUT!!!":
        życia -= 1
        print("Na szczęście nie jest to prawdziwe koło fortuny i nie tracisz całej kasy tylko tracisz 1 życie zostało ci ",życia)

    elif nagroda == "Nagroda":
        n = nagrody()
        print("Jeśli zgadniesz literę dostaniesz: ", n)
        nagroda=0
    elif nagroda == "500?":
        print("masz dwie opcje: 1.zostajesz przy 500  czy 2.odsłaniasz karte i ryzykujesz 50/50 1300 albo bankrut")
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
    nagrod={1:1000, 2:2000, 3:1050, 4:"Samochód", 5:1000, 6:3000, 7:2500, 8:1500}
    x = random.randrange(1, 9)
    for i in nagrod.keys():
        if i == x:
            return nagrod[i]



def bankrut(nagroda,życia,kasa,has,imie):
    while nagroda=="BANKRUT!!!":
        życia = życia - 1
        życia2(życia,kasa,has,imie)
        print("Wylosowałeś bankruta, zostalo ci", życia,"żyć ")
        k = input("Zakreć kołem jeszcze raz: ")
        kolo2(k)
        nagroda = krecenie(życia)

    return nagroda



def kolo2(k):
    while k != "kolo":
        k = input("Napisałeś źle kolo")



def życia2(życia,kasa, has,imie):
    if życia == 0 :
        print("Pzegrałeś, skończyły ci się życia - wygraleś: ",kasa)
        print("Hasło to : ",has)
        lista = zapisywanie()
        lista2 = dodawanie(lista, imie, str(kasa))
        sort(lista2)
        tablica_wyników(lista2)
        i = 0
        while i != 10:
            i += 1
            time.sleep(1)
        sys.exit(0)

def odgadywaniehasła(kasa,has,wynik,życia,nagroda,kategoria,imie):
    sp = 0
    sp2 = 0
    for i in has:
        for j in samogłoski:
            if i == j:
                sp += 1
    while sp !=sp2:
        ile=0
        print("Dla przypomnenia kategora hasła:", kategoria)
        litera=input("Podaj spółgłoskę ")
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
                    k = input("Napisz 'kolo' aby zakręcisz kołem ")
                    kolo2(k)
                    nagroda=krecenie(życia)
                    bankrut(nagroda, życia,kasa,has,imie)
                    nagroda=bankrut(nagroda,życia,kasa,has,imie)
                if ile==0 and sp !=sp2:
                    życia-=1
                    życia2(życia,kasa,has,imie)
                    print("Nie ma takiej literki lub już ją podałeś, tracisz jedno życie zostało ci: ",życia, " zakreć kołem jeszcze raz, aby grać dalej")

                    print(wynik)
                    k = input("Napisz 'kolo' aby zakręcisz kołem ")
                    kolo2(k)
                    nagroda = krecenie(życia)
                    nagroda=bankrut(nagroda, życia,kasa,has,imie)
        else:
            if sp != sp2:
                print("Prosze o podanie spółgłoski ")
                print(wynik)
    return kasa, życia






def czas():
    global s
    s=90
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        while s > 0:
            if s == 45:
                print("---Połowa czasu mineła---")
            time.sleep(1)
            s-= 1
        print("Czas się skończył, prosze naciśnij Enter")



def dodawanie(lista,imie,kasa):
   d={'miejsce':len(lista)+1, 'imie':imie, 'wynik':kasa}
   lista.append(d)

   return lista



def zapisywanie():
    lista = []
    with open('wyniki.csv', 'r', encoding='utf-8-sig') as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=';')
        for row in csvreader:
            lista.append(row)

        return (lista)



def sort(lista):
    n = len(lista)

    sorted_list = lista
    i = 0

    while i < n:
        k = 0

        while k < n - 1:
            if sorted_list[k]['wynik'] < sorted_list[k + 1]['wynik']:
                p = sorted_list[k]['wynik']
                p2 = sorted_list[k]['imie']
                sorted_list[k]['wynik'] = sorted_list[k + 1]['wynik']
                sorted_list[k]['imie'] = sorted_list[k + 1]['imie']
                sorted_list[k + 1]['wynik'] = p
                sorted_list[k + 1]['imie'] = p2

            k += 1
        i += 1
    return sorted_list



def tablica_wyników(lista):
        with open('wyniki.csv', 'w') as csvfile:
            csvw = csv.writer(csvfile,delimiter=';')
            csvw.writerow(['miejsce', 'imie', 'wynik'])
            for i in range(0,len(lista)):
                csvw.writerow([lista[i]['miejsce'],lista[i]['imie'],lista[i]['wynik']])
            k=0
            print("Najlepszych 5 graczy:")
            for row in lista:
                if k == 5:
                    break
                print(row['miejsce'], row['imie'], row['wynik'])
                k+=1

