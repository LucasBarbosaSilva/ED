class Celula:
    item = None
    proximo = None

    def __init__(self, item):
        self.item = item
    
class FilaEncadeada:
    inicio = None
    fim = None
    tamanho = 0

    def __init__(self):
        self.inicio = Celula(None)
        self.fim = self.inicio

    def enfileirar(self, item):
        aux = self.fim
        aux.proximo = Celula(item)
        self.fim = aux.proximo
        self.tamanho +=1

    def estaVazia(self):
        return self.tamanho == 0

    def desenfileirar(self):
        if(not(self.estaVazia())):
            atual = self.inicio
            proximo = atual.proximo
            self.inicio = proximo
            self.tamanho -=1
            if(self.tamanho == 0):
                self.fim = self.inicio

            return atual.item
        else:
            print("Fila vazia")
    
    def imprimir(self):
        aux = self.inicio.proximo
        while aux != None:
            print(aux.item)
            aux = aux.proximo
        print('---')

