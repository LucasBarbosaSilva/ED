'''
1. Implemente uma função que recebe 3 listas ordenadas e combina estas listas 
de modo que a combinação resultante é uma lista ordenada, seguindo o princípio 
de combinação do merge sort. Informe qual o custo do seu algoritmo no pior caso.
'''
#CÓDIGO ANTES DE VER A RESOLUÇÃO DO PROFESSOR:
def merge(listaI, listaII):
    listaOrdenada = [None]*(len(listaI) + len(listaII))
    i, j = 0, 0
    for x in range(len(listaOrdenada)):
        if  (i >= len(listaI)):
            listaOrdenada[x] = listaII[j]
            j+=1
        elif(j >= len(listaII)):
            listaOrdenada[x] = listaI[i]
            i+=1
        elif(listaI[i] < listaII[j]):
            listaOrdenada[x] = listaI[i]
            i+=1
        else:
            listaOrdenada[x] = listaII[j]
            j+=1
    return listaOrdenada

lista1 = [1, 4, 7, 10, 13]
lista2 = [2, 5, 8, 11]
lista3 = [0, 3, 6, 9, 12, 14, 15]

lista4 = merge(lista1, lista2)
listaFinal = merge(lista4, lista3)
print(listaFinal)

#CÓDIGO COM A RESOLUÇÃO DO PROFESSOR:
def merge2(listaI, listaII, listaIII):
    listaOrdenada = [None]*(len(listaI) + len(listaII) + len(listaIII))
    i, j, z = 0, 0, 0
    for x in range(len(listaOrdenada)):
        v1 = listaI[i] if i < len(listaI) else float('inf')
        v2 = listaII[j] if j < len(listaII) else float('inf')
        v3 = listaIII[z] if z < len(listaIII) else float('inf')

        if(v1 <= v2 and v1 <= v3):
            listaOrdenada[x] = v1
            i+=1
        elif(v2 <= v1 and v2 <= v3):
            listaOrdenada[x] = v2
            j+=1
        else:
            listaOrdenada[x] = v3
            z+=1
    return listaOrdenada

lista1 = [1, 4, 7, 10, 13]
lista2 = [2, 5, 8, 11]
lista3 = [0, 3, 6, 9, 12, 14, 15]

listaFinal = merge2(lista1, lista2, lista3)
print(listaFinal)