def czy_ddatnie(a,b,c):
    if a>0 and b>0 and c>0:
        return True
    else:
        return False


def czy_trojkat(a,b,c):
    if czy_ddatnie(a,b,c)==True:
        if a>b and a>c:
            if b+c>a:
                return True
            else:
                return False
        elif b>a and b>c:
            if a+c>b:
                return True
            else:
                return False
        elif c>b and c>a:
            if b+a>c:
                return True
            else:
                return False

    else:
        return False


print(czy_trojkat(3, 5, 8))