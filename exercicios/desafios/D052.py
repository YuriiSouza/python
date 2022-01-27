#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um número para a analise: "))
cont = 0
for c in range(2, n):
    if n % c == 0:
        cont += 1;

if cont == 0:
    print("Valor primo")
else:
    print("Valor não é primo")
