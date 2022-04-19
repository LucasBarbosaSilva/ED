import random as r
import math

d1 = str(math.floor(r.random() * 10))
d2 = str(math.floor(r.random() * 10))
d3 = str(math.floor(r.random() * 10))
d4 = str(math.floor(r.random() * 10))

senhaCorreta = '9999'
senhaEncontrada = '0000'
tentativas = 1
while(senhaEncontrada != senhaCorreta):
    tentativas += 1
    d1 = str(math.floor(r.random() * 10))
    d2 = str(math.floor(r.random() * 10))
    d3 = str(math.floor(r.random() * 10))
    d4 = str(math.floor(r.random() * 10)) 
    senhaEncontrada = d1+d2+d3+d4

print("A senha era: ", senhaCorreta)
print("Quantidade de tentativas: ", tentativas)