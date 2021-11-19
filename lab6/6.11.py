def pangram(napis):
    alfabt=["."," ","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

    for i in range (0,len(napis)):
        for j in alfabt:
            litera=napis[i]
            if litera.lower() == j:

                break
        else:
            return False

    return True


napis="The quick brown fox jumps over the lazy dog."
print(pangram(napis))


