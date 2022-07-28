# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
n = int(input("Digite a quantidades de termos da sequência: "))

cont = 0
while cont < n:
    if cont == 0:
        f = cont
        print(f)
        cont += 1
    elif cont == 1:
        f = cont
        print(f)
        cont_1 = f
        cont_2 = 0
        cont += 1
    else:
        f = cont_1 + cont_2
        print(f)
        cont_2 = cont_1
        cont_1 = f
        cont += 1
        