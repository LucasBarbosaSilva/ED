class Objeto:
    valor = None
    proximo = None
    def __init__(self, valor):
        self.valor = valor
    
class PilhaEncadeada:
    topo = None
    tamanho = 0

    def empilha(self, item):
        item.proximo = self.topo
        self.topo = item
        self.tamanho += 1

    def desempilha(self):
        if(self.tamanho > 0):
            #pegar o atual
            atual = self.topo
            #substituir o topo pelo proximo do atual
            self.topo = atual.proximo
            #decrementa o tamanho
            self.tamanho -= 1
            #retorna o item desempilhado
            return atual
        else:
            return "Vazio"

    def estaVazia(self):
        return True if self.tamanho == 0 else False

    def tamanhoPilha(self):
        return self.tamanho

def validaPalindrono(palavra):
    pilha = PilhaEncadeada()
    palavra = palavra.replace(" ", "").lower()
    tamanho = len(palavra)
    if(tamanho % 2 == 1):
        meio = palavra[tamanho//2]
        palavra = palavra.replace(meio, "")
    metade = len(palavra)//2
    for x in range(0, metade):
        letra = Objeto(palavra[x])
        pilha.empilha(letra)
    for x in range(metade, len(palavra)):
        letra = pilha.desempilha()
        if(letra.valor != palavra[x]):
            return "não"
    return "sim"

entrada = input()

print(validaPalindrono(entrada))
