a=22
b=34
while a>0:
    if a>b:
        a=a-b
    elif b>a:
        b=b-a
    else:
        break
print(a)