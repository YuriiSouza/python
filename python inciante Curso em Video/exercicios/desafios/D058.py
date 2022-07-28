#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

cont = 0
print("-="*12)
print("Advinhe o valor sorteado")
print("-="*12)
n = randint(0,11)

while True:
    cont += 1
    r = int(input("Qual valor o computador sorteou? "))
    if r == n:
        break
    else:
        print("...")
        sleep(0.5)
        print("...")
        sleep(0.5)
        print("...")
        sleep(0.75)
        print("Tente novamente...")
        if r > n:
            print("Menos...")
        else:
            print("mais...")

print("...")
sleep(0.5)
print("...")
sleep(0.5)
print("...")
sleep(0.75)
print(f"""Parabéns, você acertou...
O valor sorteado era mesmo {n}
Você acertou com {cont} tentativas...""")
