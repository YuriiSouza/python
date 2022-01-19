#Faça um programa que leia um ano e retorne se ele é bissesto.
ano = int(input("Ano: "))

if ano % 4 == 0:
    print("É um ano bissesto.")
else:
    print("Não é um ano bissesto.")
