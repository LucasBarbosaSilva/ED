'''
6. Algoritmo que recebe duas listas e imprime a
intersecção das duas listas
'''
lista1 = set([x for x in input("Digite os elementos da lista 1: ").split()])
lista2 = set([x for x in input("Digite os elementos da lista 2: ").split()])

def interseccao(l1, l2):
    interseccao = []
    for x in l1:
        if (x in l2):
            interseccao.append(x)
    return interseccao

print("A intersecção das listas é: ", interseccao(lista1, lista2))