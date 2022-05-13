def ordenaInsertion(lista):
    for i in range(1, len(lista)):
        for j in range(i-1, 0, -1):
            if(lista[j+1][1] < lista[j][1]):
                lista[j+1], lista[j] = lista[j] ,lista[j+1]
            else:
                break
    return lista

n = int(input())
listaBois = [()]*n
for x in range(n):
    id, peso = input().split()
    peso = float(peso)
    listaBois[x] = (id, peso)

ordenado = ordenaInsertion(listaBois)
print("Gordo: id:",ordenado[-1][0],"peso: %.2fKg" %ordenado[-1][1])
print("Magro: id:",ordenado[0][0],"peso: %.2fKg" %ordenado[0][1])