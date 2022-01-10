import random
import csv


global has
global wynik
global kasa
global życia
kasa=0
życia=10
wynik=[]
def kolo():
    kolo1={1:100, 2:200, 3:250, 4:400, 5:500, 6:1000, 7:3000, 8:"500?", 9:"Nagroda", 10:"BANKRUT!!!", 11:550, 12:800, 13:50, 14:100, 15:200}
    x = random.randrange(1,16)
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

def literowanie(litera, nagroda,kasa):
    wynik=odgadywanie(has)
    ile=0
    for i in range(0,len(has)):
        if has[i] == litera:
            wynik[i] = litera
            ile+=1
    return wynik

def kasowanie(nagroda,wynik,kasa):
    ile=0
<<<<<<< HEAD
    for i in range(0,len(wynik)):
        if wynik[i] == litera:
            ile+=1
    if ile != 0:
        kasa=kasa+(ile*nagroda)
=======
    if nagroda != "BANKRUT!!!":
        for i in range(0,len(wynik)):
            if wynik[i] !=" _ ":
                ile+=1
            if ile != 0:
                kasa=kasa+(ile*nagroda)

>>>>>>> cb8ccf0 (zad)
    return kasa

def krecenie(k,życia,kasa):
    if k == "kolo":
        nagroda=kolo()
        print("wylosowałeś: ", nagroda)
        if nagroda=="BANKRUT!!!":
                nagroda=0

                print("Na szczęście nie jest to prawdziwe koło fortuny i nie tracisz całej kasy tylko tracisz 1 życie zostało ci ",życia)
        elif nagroda == "Nagroda":
            print("Jeśli zgadniesz litera dostaniesz: ", nagrody())
            nagroda=0
        elif nagroda =="500?":
            print("masz dwie opcje: 1.zostajesz przy 500  czy 2.odsłaniasz karte i ryzykujesz 50/50 3500 albo bankrut")
            wybor=input("1 czy 2 ?")
            if wybor == "1":
                nagroda=500
            elif wybor == "2":
                druga=odslanianie()
                print("Po drugiej strona jest...",druga)
                if druga=="BANKRUT!!!":
                    nagroda=0
                else:
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

samogłoski=['b', 'c', 'ć', 'd', 'f','h', 'g', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż']
spółgłoski=['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó']
alfabet=['b', 'c', 'ć', 'd', 'f','h', 'g', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'p', 'r', 's', 'ś', 't', 'w', 'z', 'ź', 'ż','a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y', 'ó']


<<<<<<< HEAD

print("Witamy w kole fortuny!!!")
print("Przedstawmy naszego gościa")
imie=input("Jak sie nazywasz?")
print("Witaj", imie)
print("Już tłumacze ci zasady")
print("Na kole znajdują się: pieniadze, nagroda, bankrut, albo 500?. Jesli to wulosujesz stoisz przed wyborem, albo  500 zł albo odkrywasz karte i masz 50/50 na bankruta albo 3500zł ")
print("Po zakręceniu kołem podajesz spółgłoske, tyle ile bedzie ich w haśle, tyle razy dostaniesz wylosowane pieniadze")
print("Jeśli nie zgadniesz, lub wylosujesz bankryta  przegrywasz wszystko")
print("W każdj chwili możesz zgadywać hasło, pamietaj aby być bardzo dokładnym w podawaniu hasła ")
print("Zaczynamy")
start=input("Tak czy Nie ?")
if start=="Tak":
    print("losowanie hasła.....")
    kategoria=losowanie()
    has=haslo(kategoria)
    wynik = odgadywanie(has)
    print("Kategoria hasła to:", kategoria)
    print("Dla ułatwienia wszystkie hasła są z małych liter")
    k=input("napisz 'kolo' aby zakręcisz kołem")
    nagroda=krecenie(k,życia,kasa)

    print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
    print(wynik)
    sp=0
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
                    kasa+=ile*nagroda
                    print("Brawo Zgadłeś zgarnałeś: ", ile*nagroda,  "  aktualny stan twojej wygranej: ", kasa)
                    print(wynik)
                    k = input("Napisz 'kolo' aby zakręcisz kołem")
                    nagroda=krecenie(k, życia, kasa)
                if ile==0:
                    życia-=1
                    print("Nie ma takiej literki lub już ją podałeś, tracisz jedno życie zostało ci: ",życia, " zakreć kołem jeszcze raz, aby grać dalej")
                    print(wynik)
                    k = input("Napisz 'kolo' aby zakręcisz kołem")
                    nagroda=krecenie(k,życia,kasa)
    else:
        print("Prosze o podanie spółgłoski")
        print(wynik)
    if sp==sp2:
        print("Skończyły się spółgłoski")
        print("Czas na odggadnięcie hasła")
        print("Możesz zgadnąć lub kupić samogłoske za 200")
        k = input("napisz kup lub haslo")
        while k != "haslo":
            ile2=0
            samogłoska=input("Podaj samogłoskę")
            kasa-=200
            for i in range(0, len(has)):
                if samogłoska== wynik[i]:
                    break
                if has[i] == samogłoska:
                        wynik[i] = samogłoska
                        ile2+=1
            if ile2!=0:
                print(wynik)
                print("twoja wygrana: ", kasa)
            else:
                print("Już podałeś tą samogłoskę lub nie ma jej w haśle")
            k = input("napisz kup lub haslo")
        if k=="haslo":
            print("Masz jedną próbę , także odpowiedz bardzo szczegółowo")
            hasl=input("odpowiedź: ")
            print(has)
            if hasl==has:
                print("Brawo udało ci się odganąć hasło")
                print("Runda Finałowa")
                print("Bedziesz musiał w czasie 1 minuty odgadnać hasło")
                print("Najpierw zakręćmy kołem finałowym")

                print("Dostaniesz 3 spółgłoski(d,r,s) + 1 samogłoske(i)")
                print("Natomiast ty wybierzesz kolejne 3 spółgłoski i jedną samogłoskę")
                samogło1=input("twoja pierwsza spółgłoska")
                while czy_sp(samogło1) == "True":
                    samogło1 = input("Podaj spółgłoskę")
                samogło2 = input("twoja druga spółgłoska")
                while czy_sp(samogło2) == "True":
                    samogło2 = input("Podaj spółgłoskę")
                samogło3 = input("twoja trzecia spółgłoska")
                while czy_sp(samogło3) == "True":
                    samogło3 = input("Podaj spółgłoske")
                samo = input("A teraz samogłoska")
                while czy_sa(samo) == "True":
                        samo = input("Podaj samogłoskę")
                kategoria2 = losowanie()
                print("kategoria rundy finałowej:", kategoria2)
                has2 = haslo(kategoria2)
                wynik2 = odgadywanie(has2)
                for i in range(0, len(has2)):
                    if has2[i] == samogło1:
                        wynik2[i] = samogło1
                    if has2[i] == samogło2:
                        wynik2[i] = samogło2
                    if has2[i] == samogło3:
                        wynik2[i] = samogło3
                    if has2[i] == samo:
                        wynik2[i] = samo
                    if has2[i] == "d":
                        wynik2[i] = "d"
                    if has2[i] == "r":
                        wynik2[i] = "r"
                    if has2[i] == "s":
                        wynik2[i] = "s"
                    if has2[i] == "i":
                        wynik2[i] = "i"
                print(wynik2)
                fina=input("Czas start, podaj hasło: ")
                while fina!= has2:
                    fina=input("Zgadduj dalej: ")
                if fina==has2:
                    print("Brawo Wygrałeś")
                    print("Zobaczmy co jest w kopercie...")
                    n=finalowe()
                    print(n)
                    if n == "Samochód":
                        print("Gratulujemy wygranej", kasa, "+ Nowego samochodu")
                    else:
                        print("Gratulujemy wygranej: ", kasa+n)
                else:
                    print("Czasami się wygrywa czasami przegrywa, zobaczmy co jest w kopercie")
                    n=finalowe()
                    print(n)
                    if n == "Samochód":
                        print("Kurcze szkoda takiej fury, ale no cóż i tak wygrałeś: ", kasa)
                    else:
                        print("Mówi się trudno, może nastepnym razem, ale i tak wygrałeś: ", kasa)
=======
# kategoria=losowanie()
# has=haslo(kategoria)
#
# nagroda=500
# print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
# print(odgadywanie(has))
# print("Czas odgadnąć literę")
# litera=input("podaj literę")
# wynik=literowanie(litera,nagroda,kasa)
# print(wynik)
#
# litera=input("podaj literę")
# wynik+=literowanie(litera,nagroda,kasa)
# print(wynik)
# print(kasa)
>>>>>>> cb8ccf0 (zad)





<<<<<<< HEAD
=======
print("Witamy w kole fortuny!!!")
print("Przedstawmy naszego gościa")
imie=input("Jak sie nazywasz?")
print("Witaj", imie)
print("Już tłumacze ci zasady")
print("Na kole znajdują się: pieniadze, nagroda, bankrut, albo 500?. Jesli to wulosujesz stoisz przed wyborem, albo  500 zł albo odkrywasz karte i masz 50/50 na bankruta albo 3500zł ")
print("Po zakręceniu kołem podajesz spółgłoske, tyle ile bedzie ich w haśle, tyle razy dostaniesz wylosowane pieniadze")
print("Jeśli nie zgadniesz, lub wylosujesz bankryta  przegrywasz wszystko")
print("W każdj chwili możesz zgadywać hasło, pamietaj aby być bardzo dokładnym w podawaniu hasła ")
print("Zaczynamy")
start=input("Tak czy Nie ?")
if start=="Tak":
    print("losowanie hasła.....")
    kategoria=losowanie()
    has=haslo(kategoria)
    print("Kategoria hasła to:", kategoria)
    print("Dla ułatwienia wszystkie hasła są z małych liter")
    k=input("napisz 'kolo' aby zakręcisz kołem")
    if k == "kolo":
        nagroda=kolo()
        if nagroda!="BANKRUT!!!":
            print("wylosowałeś: ", nagroda)
            if nagroda == "Nagroda":
                print("Jeśli zgadniesz litera dostaniesz: ", nagrody())
            elif nagroda =="500?":
                print("masz dwie opcje: 1.zostajesz przy 500  czy 2.odsłaniasz karte i ryzykujesz 50/50 3500 albo bankrut")
                wybor=input("1 czy 2 ?")
                if wybor == "1":
                    nagroda=500
                elif wybor == "2":
                    druga=odslanianie()
                    print("Po drugiej strona jest...",druga)
                    if druga=="BANKRUT!!!":
                        kasa=0
                    else:
                        nagroda=druga
            print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
            print(odgadywanie(has))
            print("Czas odgadnąć literę")
            litera=input("podaj literę")
            print(literowanie(litera,nagroda,kasa))
        else:
            print("Wylosowałeś bankruta, zakręć kołem jeszcze raz")





>>>>>>> cb8ccf0 (zad)



