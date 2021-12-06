def potega(n):
    if n==1:
        return n
    return potega(n-1)+n+(n-1)
print(potega(2))