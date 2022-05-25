def busca(lista, ini, fim, chave):
    posicao = len(lista)
    if(fim>ini):
        meio = (ini+fim)//2
        if(lista[meio][0] <= chave[0] and chave[0] < lista[meio+1][0]):
            posicao = meio+1
            return posicao
        elif(lista[meio][0] < chave[0]):
            return busca(lista, meio+1, fim, chave)
        else:
            return busca(lista, ini, meio, chave)
    elif(ini == 0):
        posicao = ini
        return posicao
    else:
        return posicao

def insere(lista, chave):
    p = busca(lista, 0, len(lista)-1, chave)
    listaOrdenada = []
    i= 0
    while i < p:
        listaOrdenada.append(lista[i])
        i+=1
    listaOrdenada.append(chave)
    i = p
    while i < len(lista):
        listaOrdenada.append(lista[i])
        i+=1
    return listaOrdenada


listaContatos = []
resp = True
while (resp):
    nome = input("Digite o nome do contato que deseja inserir: ")
    numero = input("Digite o número do contato que deseja inserir: ")
    novoContato = (nome, numero)
    listaContatos = insere(listaContatos, novoContato)
    print(listaContatos)
    resp = True if input("Deseja continuar?(s/n)") == 's' else False