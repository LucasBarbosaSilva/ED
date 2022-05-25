import math

def calculaDistancia(posicaoPessoa, listaMotoristas):
    listaDistancias = [None]*(len(listaMotoristas))
    for i in range(len(listaDistancias)):
        x = (u[0] - listaMotoristas[i][1])**2
        y = (u[1] - listaMotoristas[i][2])**2
        d = math.sqrt(x+y)
        listaDistancias[i] = (listaMotoristas[i][0], d)
    return listaDistancias
#implementar usando o merge
def ordenaLista(lista1, lista2):
    listaOrdenada = [None]*(len(lista1)+len(lista2))
    i = j = 0
    for x in range(len(listaOrdenada)):
        if(i >= len(lista1)):
            listaOrdenada[x] = lista2[j]
            j+=1
        elif(j >= len(lista2)):
            listaOrdenada[x] = lista1[i]
            i+=1
        elif(lista1[i][1]< lista2[j][1]):
            listaOrdenada[x] = lista1[i]
            i+=1
        else:
            listaOrdenada[x] = lista2[j]
            j+=1
    return listaOrdenada

def divide(lista, ini, fim):
    meio = (ini+fim)//2
    if((fim-ini) == 1):
        return lista[ini:fim]
    else:
        lista1 = divide(lista, ini, meio)
        lista2 = divide(lista, meio, fim)
        return ordenaLista(lista1, lista2)

u = (10, 10)
lista = [
    ("Maria", 30, 20), 
    ("Cezar", 10, 40), 
    ("Cristofer", 30, 60),
    ("Thiago", -10, 20),
    ("João", 20, 20)
    ]
lista = calculaDistancia(u, lista)
lista = (divide(lista, 0, len(lista)))
print("O(a) motorista mais próximo é %s" %lista[0][0])