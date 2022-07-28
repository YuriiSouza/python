#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print("=="*8)
print("Criando uma P.A")
print("=="*8)
primeiroTermo = int(input("Primeiro termo da P.A: "))
razao = int(input("Razão da P.A: "))

cont = 0
while cont < 10:
    print(primeiroTermo)
    primeiroTermo += razao
    cont += 1
