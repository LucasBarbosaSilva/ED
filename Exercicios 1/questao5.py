'''
Copiar uma lista de inteiros, retirando elementos repetidos
'''
listaRepetidos = [int(x) for x in input().split()]
def retiraRepetidos(lista):
    listaUnicos = []
    for x in lista:
        if (not(x in listaUnicos)):
            listaUnicos.append(x)
    return listaUnicos

print(retiraRepetidos(listaRepetidos))
'''
Função de custo:
4 + 3n ou apenas n 
'''