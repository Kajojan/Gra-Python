for i in range(100,999):
    liczba=i
    a=liczba%10

    liczba=liczba//10
    b=liczba%10

    liczba=liczba//10
    c=liczba

    if a > b and a > c:
        if c == b:
            print(a,b,c)
        elif c > b:
            print(a,c,b)
        else:
            print(a,b,c)

    elif b > a and b > c:
        if a == c:
            print(b,c,a)
        elif c > a:
            print(b,c,a)
        else:
            print(b,a,c)

    elif c > b and c > a:
        if a == b:
            print(c,a,b)
        elif b > a:
            print(c,b,a)
        else:
            print(c,a,b)


