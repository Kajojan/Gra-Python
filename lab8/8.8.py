def nwd(a,b):
    if a == b:
        return a
    if a > b:
        a=a-b
    if b > a:
        b= b-a
    return nwd(a,b)
print(nwd(6,24))