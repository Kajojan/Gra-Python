a = 1
b = 6
c = 9
delta = b**2 - 4*a*c
if a == 0 and b!=0:
    x = b/c
    print("jedno miejsce zerowe\n",x," ",0)
elif delta > 0:
    print("2 miejsca zerowe")
elif delta == 0:
    x = (-b)/(2*a)
    print("jedno miejsce zerowe\n", x, " ", 0)
elif delta < 0:
    print("brak miejsca zerowego")




