'''
Identificar os valores de um conjunto que estão abaixo da
média do conjunto
'''
continua = True
soma = 0
elementos = []
while (continua):
    ele = float(input("Informe um elemento: "))
    soma += ele
    elementos.append(ele)
    resp = input("Deseja informar mais algum elemento? (S/N) ")
    if(resp.lower() == 'n' ):
        continua = False
media = soma / len(elementos)
print("A media do conjunto é:", media)

def verificaAbaixoMedia(m, elem):
    for x in elem:
        if(x < m):
            print(x,"está abaixo da média do conjunto")

verificaAbaixoMedia(media, elementos)

'''
Função do conjunto:
5 + 7n
Ou apenas n
'''