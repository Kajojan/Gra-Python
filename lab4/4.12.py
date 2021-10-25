napis="bacabc"
wzorzec="abc"
tak=0
for i in range (0,len(napis)):
    if napis[i:len(wzorzec)+i]== wzorzec:
        tak=tak+1
if tak !=0:
    print("tak")
else:
    print("Nie")

