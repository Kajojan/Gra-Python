def parzyste(n):
    if  n==2:
        return n
    return parzyste(n-2)+n

print(parzyste(8))