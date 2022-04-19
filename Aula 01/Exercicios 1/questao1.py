'''
Contar o número de elementos negativos em um conjunto
'''
conjunto = [float(x) for x in input().split()]

def quantidadeNegativos(conj):
    cont = 0
    for x in conj:
        if x < 0:
            cont+=1
    return cont

print("Quantidade de números negativos é:", quantidadeNegativos(conjunto)) 

'''
Função de custo:
2n + 2
ou apenas n
'''