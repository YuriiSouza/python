# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
from time import sleep

cont = 0
while True:
    player = int(input("[1]IMPAR\n[2]PAR\n"))
    playerNum = int(input("Digite um valor:"))
    pc = randint(0,11)

    fator = (pc + playerNum) % 2

    if (fator == 0 and player == 2) or (fator == 1 and player == 1):
        print("O resultado foi ")
        sleep(0.4)
        print("...")
        sleep(0.4)
        print(pc + playerNum)
        print("GANHOUU")
        cont += 1
    else:
        print("O resultado foi ")
        sleep(0.4)
        print("...")
        sleep(0.4)
        print(pc + playerNum)
        print("perdeu, até mais...")
        break
print(f"Você ganhou {cont} vezes...")