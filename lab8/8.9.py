def suma(liczba):
    if liczba < 10:
        return liczba
    return suma(liczba //10)+suma(liczba%10)


liczba1 = 123
print(suma(liczba1))
