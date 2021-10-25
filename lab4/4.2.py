slowo="annaaaaa"
lista=["a", "ą", "e", "ę", "i", "o", "u", "y"]
ile=0
for i in range (0, len(slowo)):
    for j in lista:
        if slowo[i] == j:
            ile+=1
print(ile)
