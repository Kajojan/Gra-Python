import random
def lista(n):
    lista1=[]
    i=0
    while i < n:
        x=random.randint(-100,100)
        lista1.append(x)
        i+=1
    return lista1

def sort(n):
    lista1=lista(n)
    print(lista1)
    sorted_list=lista1
    i=0

    while i < n:
        k = 0
        while k < n-1:
            if sorted_list[k] > sorted_list[k+1]:
                p=sorted_list[k]
                sorted_list[k]=sorted_list[k+1]
                sorted_list[k+1]=p
            k+=1
        i+=1
    return sorted_list

print(sort(3))

