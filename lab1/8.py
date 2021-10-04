a = 12311
b = 1221
c = 1101
if a > b:
    if c > a:
        print(c , a , b)
    else:
        print(a,c,b)
elif b > a:
    if c > b:
        print(c , b , a)
    else:
        print(b,c,a)
elif b > c:
    if a > b:
        print(a , b, c)
    else:
        print(b,a,c)
