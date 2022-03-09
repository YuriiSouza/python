#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = float(input("Valor: "))

notas50 = valor // 50

valor20 = valor % 50
notas20 = valor20 // 20

valor10 = valor20 % 20
notas10 = valor10 // 10

valor1 = valor10 % 10
notas1 = valor1 // 1

print(f"""Notas R$50,00: {notas50:.0f}
Notas R$20,00: {notas20:.0f}
Notas R$10,00: {notas10:.0f}
Notas R$1,00: {notas1:.0f}""")