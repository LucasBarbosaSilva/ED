'''
3. O algoritmo insertion sort funciona inserindo o i-ésimo elemento na posição 
correta na ordenação. Para isso, ele verifica a posição correta desse valor do início 
até a posição i, que se mantém sempre ordenada. O custo para se inserir o elemento i 
na posição correta é O(n) no pior caso. Você, que é um cientista da computação muito esperto, 
identificou que usando a busca binária, você pode reduzir o custo de inserção para O(logn) 
fazendo uma busca binária para encontrar a posição correta para inserir o elemento i 
a cada rodada do algoritmo. Implemente a função que, utilizando busca binária, recebe uma 
lista ordenada e um valor v e retorna a posição na lista onde v deve ser inserido para 
que a lista permaneça ordenada.
'''

#SOLULÇÃO APÓS CONFERIR A RESPOSTA DO PROFESSOR:
def insertionBuscaBinaria2(lista, inicio, fim, chave):
    if inicio > fim:
        return inicio
    meio = (inicio+fim)//2
    
    if chave == lista[meio]:
        return meio
    else:
        if chave < lista[meio]:
            return insertionBuscaBinaria2(lista,inicio,meio-1,chave)
        else:
            return insertionBuscaBinaria2(lista,meio+1,fim,chave)
lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(insertionBuscaBinaria2(lista1, 0, len(lista1), 4))
print(insertionBuscaBinaria2(lista1, 0, len(lista1), 16))