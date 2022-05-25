class Celula:
    valor = None
    proximo = None

    def __init__(self, item):
        self.item = item

class Pilha():
    topo = None
    tamanho = 0

    def empilha(self, item):
        item.proximo = self.topo
        self.topo = item
        self.tamanho+=1
    
    def desempilha(self):
        #obter o elemento do topo
        atual = self.topo
        #obter o proximo do topo
        proximo = atual.proximo
        #topo recebe o proximo
        self.topo = proximo
        #diminuir tamanho
        self.tamanho-=1
        #return
        return atual
    
    def imprimePilha(self):
        item = self.topo
        tamanho = self.tamanho
        while (tamanho>0):
            print(item.valor)
            item = item.proximo
            tamanho-=1


