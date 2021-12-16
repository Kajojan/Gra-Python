def spr_18(pesel,data):
    if pesel==int(pesel):
        rok = pesel//1000000000 + 1900
        miesac_pomoc = pesel//10000000
        miesiac=miesac_pomoc%100
        dzien_pomoc=pesel//100000
        dzien=dzien_pomoc%100
        if data[2]-rok==18:
            if data[1]>=miesiac:
                if data[0]>=dzien:
                    return True
        else:
            return False
    if pesel== str(pesel):



def test_spr_18():
    pesel = 99112409495
    data = [24, 11, 2010]
    assert spr_18(pesel,data) == False
