#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint


tabela = [[], []]
n = int(input("How many games you want? "))

for x in range(0, n):
    for l in range(0, 2):
        for c in range(0, 3):
            tabela[l].append(randint(0, 61))

    for l in range(0, 2):
        print(" ")
        for c in range(0, 3):
            print(tabela[l][c], end = " ")
    print(" ")
    print("=-"*20)
    