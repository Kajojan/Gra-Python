def silnia(n):



    if n==1:

        return n

    else:


        return silnia(n-1)*n

print(silnia(3))