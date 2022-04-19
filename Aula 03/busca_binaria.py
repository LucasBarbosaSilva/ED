lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def busca_binaria(comeco, fim, elemento):
    global lista
    if(fim < comeco):
        return "Não existe esse elemento na lista"
    meio = comeco+((fim + comeco)//2)
    if(lista[meio] == elemento):
        return meio
    elif(lista[meio] > elemento):
        return busca_binaria(comeco, meio-1, elemento)
    else:
        return busca_binaria(meio+1, fim, elemento)

print(busca_binaria(0, len(lista)-1, 10))
'''
0 9 10
4 -> 5 < 10
    5 9 10

7 -> 8 < 10
    8 9 10
8 -> 9 < 10

6 -> 7 != 8
7 < 8
    6 9 8

7 -> 8 == 8
'''
