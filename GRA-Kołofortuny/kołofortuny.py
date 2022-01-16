from funkcje import *
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
    kolo2(k)
    nagroda=krecenie(życia)
    bankrut(nagroda,życia)
    print("Wylosowałeś nagrode to czas na odgadywanie o to zaczyfrowane haslo")
    print(wynik)
    czy=odgadywaniehasła(kasa,has,wynik,życia,nagroda)


    if czy==True:
        print("Skończyły się spółgłoski")
        print("Czas na odggadnięcie hasła")
        print("Możesz zgadnąć lub kupić samogłoske za 200")
        k = input("napisz kup lub haslo")
        while k != "haslo":
            ile2=0
            samogłoska=input("Podaj samogłoskę")
            kasa-=200
            if kasa<0:
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














