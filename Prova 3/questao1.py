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
        self.tamanho = self.tamanho + 1

    def desempilha(self):
        if(self.tamanho > 0):
            #pegar o atual
            atual = self.topo
            #substituir o topo pelo proximo do atual
            self.topo = atual.proximo
            #decrementa o tamanho
            self.tamanho = self.tamanho - 1
            #retorna o item desempilhado
            return atual
        else:
            return "Vazio"

    def estaVazia(self):
        return True if self.tamanho == 0 else False

    def tamanhoPilha(self):
        return self.tamanho

def validaFormula(string):
    pilhaParenteses = PilhaEncadeada()
    pilhaColchetes = PilhaEncadeada()
    pilhaChaves = PilhaEncadeada()
    for x in string:
        letra = Objeto(x)
        if(letra.valor == "("):
            pilhaParenteses.empilha(letra)
        elif(letra.valor == ")"):
            if(pilhaParenteses.desempilha() == "Vazio"):
                return "não"
        elif(letra.valor == "["):
            pilhaColchetes.empilha(letra)
        elif(letra.valor == "]"):
            if(pilhaColchetes.desempilha() == "Vazio"):
                return "não"
        elif(letra.valor == "{"):
            pilhaChaves.empilha(letra)
        elif(letra.valor == "}"):
            if(pilhaChaves.desempilha() == "Vazio"):
                return "não"

    if(pilhaChaves.estaVazia() and pilhaColchetes.estaVazia() and pilhaParenteses.estaVazia()):
        return "sim"
    else:
        return "não"

entrada = input()

print(validaFormula(entrada))