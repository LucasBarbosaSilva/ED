#Selecion: 
    #Seleciona um índice i
    #Troca com o menor da lista

def selecionSort(lista):
    for i in range(0, len(lista)-1):
        menor = i
        for j in range(i, len(lista)):
            if(lista[j] < lista[menor]):
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

print(selecionSort([ 41, 8, 87,	 64, 2, 97,	 56, 2, 88, 14]))