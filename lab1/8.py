a = 1103
b = 1101
c = 1102
#a
if a > b and a > c:
    if c == b:
        print("c= ",c ,"b= ", b,"a= " ,a ,"\nc=b<a")
    elif c > b:
        print("a= " ,a ,"c= ",c ,"b= ", b, "\na>c>b")
    else:
        print("a= " ,a,"c= ",c,"b= ",b, "\nc=b<a")
#b
elif b > a and b > c:
    if a == c:
        print("c= ",c ,  "a= " ,a,"b= ",b ,"\nc=a<b")
    elif c > a:
        print("b= ",b,"c= ",c,"a= " ,a, "\nb>c>a")
    else:
        print("b= ",b,"a= " ,a,"c= ",c,"\nb>a>c")
#c
elif c > b and c > a:
    if a == b:
        print("c= ",c,"a= " ,a ,"b= ", b, "\na=b<c")
    elif b > a:
        print("c= ",c,"b= ",b,"a= " ,a, "\nc>b>a")
    else:
        print("c= ",c,"a= " ,a,"b= ",b,"\nc>a>b")

elif a == c and c==b:
        print("a=c=b")
