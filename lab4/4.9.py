lista1=[1,2,3,4]
lista2=[6,5,6]
tak=0
for i in lista1:
    for j in lista2:
        if i == j:
            tak=tak+1
if tak !=0:
    print("Tak")
else:
    print("Nie")