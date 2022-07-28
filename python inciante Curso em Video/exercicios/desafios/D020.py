#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostra a ordem sorteada.
from random import shuffle
nome1 = input("Nome 1: ")
nome2 = input("Nome 2: ")
nome3 = input("Nome 3: ")
nome4 = input("Nome 4: ")

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print(lista)

