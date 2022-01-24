from funkcje import *
import time
import threading
global has
global wynik
global kasa
global życia
kasa=0
życia=10
wynik=[]
print("Witamy w kole fortuny!!!")
print("Przedstawmy naszego gościa")
imie=input("Jak sie nazywasz?")
print("Witaj", imie)
print("Już tłumacze ci zasady")
print("Na kole znajdują się: pieniadze, nagroda, bankrut, albo 500?. ")
time.sleep(3)
print("Po zakręceniu kołem podajesz spółgłoske, tyle ile bedzie ich w haśle, tyle razy dostaniesz wylosowane pieniadze")
time.sleep(4)
print("Jeśli nie zgadniesz, lub wylosujesz bankrut  tracisz życie, na start masz ich 10")
time.sleep(3)
print("Pamietaj aby być bardzo dokładnym w pisowni ")
time.sleep(3)
print("Zaczynamy")
start=input("Tak czy Nie ? ")
while start != "Tak" and start != "Nie":
    start=input("Widać, ze nie czytałeś tego co napisalem. Napisz uwzdlędniajac wielkie litery: ")
if start=="Tak":
    print("losowanie hasła.....")
    time.sleep(2)
    kategoria=losowanie()
    has=haslo(kategoria)
    wynik = odgadywanie(has)
    print("Kategoria hasła to:", kategoria)
    print("Dla ułatwienia wszystkie hasła są z małych liter")
    k=input("napisz 'kolo' aby zakręcisz kołem ")
    kolo2(k)
    nagroda=krecenie(życia)
    nagroda=bankrut(nagroda,życia,kasa,has)
    print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
    print(wynik)
    kasa,życia=odgadywaniehasła(kasa,has,wynik,życia,nagroda,kategoria)
    if True:
        print("Brawo Zgadłeś, aktualny stan twojej wygranej: ", kasa)
        time.sleep(1)
        print("Skończyły się spółgłoski")
        time.sleep(1)
        print("Czas na odgadnięcie hasła")
        time.sleep(1)
        print("Możesz zgadnąć lub kupić samogłoske za 200")
        k = input("napisz kup lub haslo ")
        while k != "kup" and k != "haslo":
            k=input("Napisałes coś źle. Napisz 'kup' albo 'haslo': ")
        while k != "haslo":
            ile2=0
            samogłoska=input("Podaj samogłoskę")
            kasa-=200
            if kasa<=0:
                kasa=0
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
            while k != "kup" and k != "haslo":
                k = input("Napisałes coś źle. Napisz 'kup' albo 'haslo': ")
        if k=="haslo":
            print("Masz jedną próbę , także odpowiedz bardzo szczegółowo")
            hasl=input("odpowiedź: ")
            if hasl==has:
                print("Brawo udało ci się odganąć hasło")
                time.sleep(2)
                print("Runda Finałowa")
                time.sleep(1)
                print("Bedziesz musiał w czasie 1,5 minuty odgadnać hasło")
                time.sleep(2)
                k=input("Najpierw zakręćmy kołem finałowym: ")
                kolo2(k)
                print("Wylosowałeś koperte, jak odgadniesz hasło zobaczysz co jest w srodku")
                time.sleep(2)
                print("Dostaniesz 3 spółgłoski(d,r,s) + 1 samogłoske(i)")
                time.sleep(2)
                print("Natomiast ty wybierzesz kolejne 3 spółgłoski i jedną samogłoskę")
                samogło1=input("twoja pierwsza spółgłoska ")
                while czy_sp(samogło1) != True:
                    samogło1 = input("Podaj spółgłoskę ")
                samogło2 = input("twoja druga spółgłoska ")
                while czy_sp(samogło2) != True:
                    samogło2 = input("Podaj spółgłoskę ")
                samogło3 = input("twoja trzecia spółgłoska ")
                while czy_sp(samogło3) != True:
                    samogło3 = input("Podaj spółgłoske ")
                samo = input("A teraz samogłoska ")
                while czy_sa(samo) != True:
                        samo = input("Podaj samogłoskę ")
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
                print("Czas start")
                fina=" "
                czas_thread = threading.Thread(target=czas)
                czas_thread.start()
                while  fina!=has2 and czas_thread.is_alive():
                    fina = input("Zgadnij hasło: ")
                if fina==has2:
                    czas_thread.daemon
                    czas_thread.do_run=False
                    print("Brawo Wygrałeś")
                    print("Zobaczmy co jest w kopercie...")
                    time.sleep(2)
                    n=finalowe()
                    print(n)
                    if n == "Samochód":
                        print("Gratulujemy wygranej", kasa, "+ Nowego samochodu")
                    else:
                        kasa+=n
                        print("Gratulujemy wygranej: ", kasa)
                else:
                    print("Czasami się wygrywa czasami przegrywa, zobaczmy co jest w kopercie")
                    n=finalowe()
                    print(n)
                    if n == "Samochód":
                        print("Kurcze szkoda takiej fury, ale no cóż i tak wygrałeś: ", kasa)
                    else:
                        print("Mówi się trudno, może nastepnym razem, ale i tak wygrałeś: ", kasa)
                lista=zapisywanie()
                lista2=dodawanie(lista,imie,str(kasa))
                sort(lista2)
                tablica_wyników(lista2)
elif start=="Nie":
    print("Do widzenia")











