import math
def busca_binaria(comeco, fim, elemento, lista):
    if(fim < comeco):
        print("Não existe esse elemento na lista")
        return 
    meio = comeco+((fim + comeco)//2)
    if(lista[meio] == elemento):
        return meio
    elif(lista[meio] > elemento):
        return busca_binaria(comeco, meio-1, elemento, lista)
    else:
        return busca_binaria(meio+1, fim, elemento, lista)

def mediana():
    return

listaInput =[int(x) for x in input("Informe1 os elementos da lista: ").split()]
num = int(input("Número a ser procurado: "))
separador = len(listaInput)//4 
posicao = busca_binaria(0, len(listaInput), num, listaInput)
cont = 1
for x in range(separador, len(listaInput), separador):
    if(posicao < x):
        print("O número está no %dº quartil" %cont)
