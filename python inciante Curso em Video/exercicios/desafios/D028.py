#Escreva um programa que faça o computador geral um número aleatória de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programe deverá escrever na tela se o usuário vencer ou perdeu.
from random import randint

n = randint(0, 5)
n1 = int(input("Advinha o número de o a 5 selecionado pelo sistema..."))

if n == n1:
    print("YOU WIN..")
else:
    print("YOU LOSE..")
    print("O numero correto era {}".format(n))
