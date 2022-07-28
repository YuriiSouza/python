#Um professor quer sortear um dos 4 alunos para apagoar o quadra. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
from random import randint


aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

sorteado = randint(1, 4)

if (sorteado == 1):
    print("O aluno sorteado foi {}".format(aluno1))
elif (sorteado == 2):  
    print("O aluno sorteado foi {}".format(aluno2))
elif (sorteado == 3):
    print("O aluno sorteado foi {}".format(aluno3))
elif(sorteado == 4):
    print("O aluno sorteado foi {}".format(aluno4))
