'''
Descrição
No frigorífico do senhor Ambrósio, existem n bois. Cada boi traz preso em seu pescoço um cartão 
contendo seu número de identificação e seu peso. Faça um programa que escreva a identificação e o 
peso do boi mais gordo e do mais magro. Considere que os bois não têm pesos iguais.

Formato de entrada:
Um inteiro n indicando a quantidade de bois do frigorifico, depois n identificadores e pesos de cada boi. 
Os identificadores são números inteiros. Os pesos de cada boi são números reais.

Formato de saída:
Duas linhas escritas:
Gordo: id: i1 peso: p1Kg
Magro: id: i2 peso: p2Kg

O peso deve ser formatado em duas casas decimais.
'''
def ordenaSelecion(lista):
    for i in range(0, len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if(lista[j][1] < lista[i][1]):
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista




n = int(input())
listaBois = [()]*n
for x in range(n):
    id, peso = input().split()
    peso = float(peso)
    listaBois[x] = (id, peso)

ordenado = ordenaSelecion(listaBois)
print("Gordo: id:",ordenado[-1][0],"peso: %.2fKg" %ordenado[-1][1])
print("Magro: id:",ordenado[0][0],"peso: %.2fKg" %ordenado[0][1])
print(ordenado)


'''
3
1 800.00
2 1000.00
3 900.00
'''