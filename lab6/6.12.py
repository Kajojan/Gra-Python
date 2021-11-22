def lata_to_min(lata):
    result = 0
    l=lata
    minuty=525600
    for i in range(0,lata):
        if l%4==0:
            result=result+minuty+1440

        else:
            result=result+minuty

    return  result

print(lata_to_min(16))



