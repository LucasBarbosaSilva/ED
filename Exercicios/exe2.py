'''
2. Um vetor v tem um pivô natural v_p se todo elemento v_i 
que vem antes da posição p é menor ou igual a v_i (v_i <= v_p, 
para todo i < p) e todo elemento v_j que vem depois da posição 
p é maior que v_p (v_p < v_j, para todo j > p). 
O primeiro e o ultimo elemento não podem ser pivôs. 
Implemente uma função que recebe uma lista e retorna a posição 
do pivô natural, caso ele exista. Informe o custo do seu algoritmo no pior caso.
'''

def encontraPivo(lista):
    p = 0
    for x in range(1, len(lista)-1):
        i = x -1
        while i >= 0 and lista[i] < lista[x]:
            i-=1
        if(i < 0):
            j = x +1
            while j < len(lista) and lista[x] < lista[j]:
                j+=1
            if(j == len(lista)):
                p = x
                return p
    return None
    

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista2 = [1,5,3,2,6,8,7,10]
lista3 = [-5,-2,-4,-3,0,5,2]
print(encontraPivo(lista1))
print(encontraPivo(lista2))
print(encontraPivo(lista3))