class Fila():
    lista = None
    inicio = None
    fim = None
    tamanho = None

    def __init__(self, tamanho):
        self.lista = [None]*tamanho
        self.inicio = self.fim = 0
        self.tamanho = tamanho

    def estaVazia(self):
        return self.inicio == self.fim

    def estaCheia(self):
        return (self.fim+1)%self.tamanho == self.inicio

    def enfileirar(self, item):
        if not self.estaCheia():
            self.lista[self.fim] = item
            self.fim = (self.fim+1)%self.tamanho
            return "Item enfileirado"
        else:
            return "Fila cheia"

    def desenfileirar(self):
        if not self.estaVazia():
            item = self.lista[self.inicio]
            self.inicio = (self.inicio+1)%self.tamanho
            return item
        else:
            print("Fila vazia")
            return

    def imprimir(self):
        i = self.inicio
        while i != self.fim:
            print(self.lista[i])
            i = (i+1)%self.tamanho
