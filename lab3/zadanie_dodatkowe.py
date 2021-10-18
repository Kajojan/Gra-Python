a=4
b=8
wynik=0
while b>0:
    if b%2!=0:
        wynik=wynik+a
    a <<=1
    b >>=1
print(wynik)