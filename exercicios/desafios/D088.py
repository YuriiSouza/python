#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

number = cont = 0
tabela = list()
todasTabelas = list()

n = int(input("How many games you want? "))

for x in range(0, n):
    tabela.clear()
    cont = 0
    while True:
        number = randint(1, 60)
        if number not in tabela:
            tabela.append(number)
            cont = cont + 1;
        if cont >= 6:
            break;
    
    todasTabelas.append(tabela[:])

for x in range(0, len(todasTabelas)):
    print(todasTabelas[x])
