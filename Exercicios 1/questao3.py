'''
Calcular o fatorial de um número
'''


def calculaFatorial(num):
    global fatorial
    if(not(num-1 == 0)):
        fatorial = fatorial * (num-1)
        calculaFatorial(num-1)
    return fatorial

n = int(input("Informe o número: "))
fatorial = n
print("O fatorial do número", n,"é:"+ str(calculaFatorial(n)))

'''
Função de custo:
n
'''