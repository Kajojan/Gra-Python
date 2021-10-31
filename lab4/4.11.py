setki=["sto", "dwieście", " trzysta", "czterysta", "Piętset", "sześćset", "siedemset", "osiemset", "dziewięćset"]
dziesiatki=["dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
jednosci=[" jeden", "dwa", "trzy","cztery", "pięć", "sześć", "siedem", "osiem", "dziewieć"]
n=998
if n<1000:
    j=n%10
    n=n//10
    napis1=jednosci[j-1]
    j = n % 10
    n = n // 10
    napis2=dziesiatki[j-1]
    j = n % 10
    n = n // 10
    napis3=setki[j-1]
    print(napis3+" "+napis2+" "+napis1)
else :
    print("podaj liczbe mniejsza od 1000")



