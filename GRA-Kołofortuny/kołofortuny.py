import random
import csv
global has
global wynik
global kasa
global życia
kasa=0
życia=5
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
        if odp[i]==" ":
            odp[i]="    "
        else:
            odp[i]=' _ '

    return odp

def literowanie(litera, nagroda,kasa):
    wynik=odgadywanie(has)
    ile=0
    for i in range(0,len(has)):
        if has[i] == litera:
            wynik[i] = litera
            ile+=1
    if ile != 0:
        kasa=kasa+(ile*nagroda)
    return wynik

def kasowanie(litera,wynik,kasa):
    ile=0
    for i in range(0,len(wynik)):
        if wynik[i] !=" _ ":
            ile+=1
    if ile != 0:
        kasa=kasa+(ile*nagroda)
    return kasa



kategoria=losowanie()
has=haslo(kategoria)

nagroda=500
print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
print(odgadywanie(has))
print("Czas odgadnąć literę")
litera=input("podaj literę")
wynik=literowanie(litera,nagroda,kasa)
print(wynik)

litera=input("podaj literę")
wynik+=literowanie(litera,nagroda,kasa)
print(wynik)
print(kasa)





# print("Witamy w kole fortuny!!!")
# print("Przedstawmy naszego gościa")
# imie=input("Jak sie nazywasz?")
# print("Witaj", imie)
# print("Już tłumacze ci zasady")
# print("Na kole znajdują się: pieniadze, nagroda, bankrut, albo 500?. Jesli to wulosujesz stoisz przed wyborem, albo  500 zł albo odkrywasz karte i masz 50/50 na bankruta albo 3500zł ")
# print("Po zakręceniu kołem podajesz spółgłoske, tyle ile bedzie ich w haśle, tyle razy dostaniesz wylosowane pieniadze")
# print("Jeśli nie zgadniesz, lub wylosujesz bankryta  przegrywasz wszystko")
# print("W każdj chwili możesz zgadywać hasło, pamietaj aby być bardzo dokładnym w podawaniu hasła ")
# print("Zaczynamy")
# start=input("Tak czy Nie ?")
# if start=="Tak":
#     print("losowanie hasła.....")
#     kategoria=losowanie()
#     has=haslo(kategoria)
#     print("Kategoria hasła to:", kategoria)
#     print("Dla ułatwienia wszystkie hasła są z małych liter")
#     k=input("napisz 'kolo' aby zakręcisz kołem")
#     if k == "kolo":
#         nagroda=kolo()
#         print("wylosowałeś: ", nagroda)
#         if nagroda=="BANKRUT!!!":
#                 kasa=0
#                 życia-=1
#                 print("Na szczęście nie jest to prawdziwe koło fortuny i nie tracisz całej kasy tylko tracisz 1 życie zostało ci ",życia)
#         elif nagroda == "Nagroda":
#             print("Jeśli zgadniesz litera dostaniesz: ", nagrody())
#         elif nagroda =="500?":
#             print("masz dwie opcje: 1.zostajesz przy 500  czy 2.odsłaniasz karte i ryzykujesz 50/50 3500 albo bankrut")
#             wybor=input("1 czy 2 ?")
#             if wybor == "1":
#                 nagroda=500
#             elif wybor == "2":
#                 druga=odslanianie()
#                 print("Po drugiej strona jest...",druga)
#                 if druga=="BANKRUT!!!":
#                     kasa=0
#                 else:
#                     nagroda=druga
#         print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
#         print(odgadywanie(has))
#         print("Czas odgadnąć literę")
#         litera=input("podaj literę")
#         print(literowanie(litera,nagroda))





