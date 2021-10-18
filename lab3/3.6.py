n=12
b=n
dzielnik=0
while b>0:
    if n%b==0:
        dzielnik=dzielnik+1
    b=b-1
print(dzielnik)