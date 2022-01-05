import random
import csv
def kolo():
    kolo1={1:100, 2:250, 3:500, 4:550, 5:800, 6:1000, 7:3000, 8:"500?", 9:"Nagroda", 10:"BANKRUT!!!"}
    x = random.randrange(1,11)
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

def haslo():
    with open('kategorie.csv', encoding='utf-8') as csvfile:
        kategorie = csv.reader(csvfile, delimiter=';')
        x = losowanie()

        for row in kategorie:
            if row[0] == x:
                k = random.randrange(1,91)
                haslo=row[k]
                return(haslo)


def odgadywanie():
    x=haslo()
    odp=[]
    for i in x:
        odp.append(i)
    for i in range(len(x)):
        if odp[i]==" ":
            odp[i]="    "
        else:
            odp[i]=' _ '

    return odp
print(odgadywanie())

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
#
#     print("Kategoria hasła to:",losowanie())
