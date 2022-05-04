#Insertion Sort
    #Seleciona o i-nésimo termo
    #Compara com os termos anteriores a ele e insere no local certo

def insertionSort(lista):
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if(lista[j] < lista[j-1]):
                lista[j], lista[j-1] = lista[j-1], lista[j]
            else:
                break
    return lista

print(insertionSort([ 41, 8, 87, 64, 2, 97, 56, 2, 88, 14]))