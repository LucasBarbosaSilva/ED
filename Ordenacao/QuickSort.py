'''
Essa divisão é feita escolhendo-se um pivô
– Coloca-se todos os elementos menores que o pivô na
primeira lista
– Coloca-se todos os elementos maiores que o pivô na
segunda lista
'''
def divide(lista):

def sort(lista):
    pivo = len(lista)//2
    if(pivo == 0):
        return lista
    else:
        i, j = 0, len(lista)-1
        while(i < j):
            if(lista[i] > lista[pivo] and lista[j] < lista[pivo]):
                lista[i], lista[j] = lista[j], lista[i]
                i+=1
                j-=1
            elif(lista[i] < lista[pivo]):
                i+=1
            else:
                j-=1
        return lista