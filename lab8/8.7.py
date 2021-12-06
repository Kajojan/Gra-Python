def pot(a, b):
    if b==1:
        return a
    return pot(a, b - 1)*a


print(pot(3, 3))
