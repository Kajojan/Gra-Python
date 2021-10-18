n=111001
m=0
suma=0
while n>0:
    suma=suma+(n%10)*(2**m)
    m=m+1
    n=n//10
print(suma)