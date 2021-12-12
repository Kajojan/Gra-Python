litery={'a':"c", 'ą':'d', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'ę':'i', 'f':'j','g':'k','h':'l', 'i':'ł', 'j':'m','k':'n','l':'ń','ł':'o','m':'ó','n':'p','ń':'r','o':'s','ó':'ś','p':'t','r':'u','s':'w','ś':'y','t':'z','u':'ż','w':'ź','y':'a','z':'ą','ż':'b','ź':'b'}


slowo ="MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG"
slowo=slowo.lower()
slowo2=""
for i in range(0,len(slowo)):
 for j in litery.keys():
  if slowo[i]==" " or slowo[i]==",":
   slowo2+=slowo[i]
   break
  elif slowo[i]==j:
   slowo2+=litery[j]


print(slowo2)
def odszyfr(slowo):
 slowo2=""
 for i in range (0,len(slowo)):
  for j in litery.keys():
   if slowo[i] == " " or slowo[i] == ",":
    slowo2 += slowo[i]
    break
   elif slowo[i] == litery[j]:
    slowo2+=j
    break
 return slowo2

print(odszyfr(slowo2))

