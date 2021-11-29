def sort(lista):
    n=len(lista)
    print(lista)
    sorted_list=lista   
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

lista=[1,2,3,4,4,1,2,9,8,7,6]
print(sort(lista))