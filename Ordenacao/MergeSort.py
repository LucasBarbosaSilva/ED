def divide(lista):
    if(len(lista)== 1):
        return lista
    else:
        meio = len(lista)//2
        lista1 = divide(lista[:meio])
        lista2 = divide(lista[meio:])
        return merge(lista1, lista2)

def merge(listaI, listaII):
    total = len(listaI) + len(listaII)
    listaOrdenada = [None]*total
    i, j = 0, 0
    for x in range(total):
        if(i == len(listaI)):
            listaOrdenada[x] = listaII[j]
            j+=1
        elif(j == len(listaII)):
            listaOrdenada[x] = listaI[i]
            i+=1
        elif(listaI[i] < listaII[j]):
            listaOrdenada[x] = listaI[i]
            i+=1
        else:
            listaOrdenada[x] = listaII[j]
            j+=1
    return(listaOrdenada)

lista = [ 41, 8, 87, 64, 2, 97, 56, 2, 88, 14]
print(divide(lista))