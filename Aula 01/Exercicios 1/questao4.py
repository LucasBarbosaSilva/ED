'''
4. Identificar a soma máxima entre dois elementos de um
conjunto
'''
def calculaMaiorSoma():
    encerrou = False
    segundoMaior = 0
    primeiroMaior = 0
    while (not(encerrou)):
        n = int(input("Informe um número: "))
        if (n > primeiroMaior):
            primeiroMaior = n
        elif (n > segundoMaior):
            segundoMaior = n
        resp = input("Deseja informar mais um número? (s/n)")
        encerrou = True if (resp.lower() == 'n') else False     
    return primeiroMaior + segundoMaior       

print("A maior soma desse conjunto é:", calculaMaiorSoma())

