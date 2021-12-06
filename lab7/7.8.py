def pierwiastek_2(x):
    pierwszy=1
    ostatni=x
    while ostatni - pierwszy > 1:
        s=(ostatni+pierwszy)//2
        if s*s==x:
            return True
        if s*s > x:
            ostatni = s
        if s*s < x:
            pierwszy = s
    return False

print(pierwiastek_2(20))
