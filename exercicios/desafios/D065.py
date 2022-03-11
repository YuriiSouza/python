# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = 0
cont = 0
maior = 0
r = ""
while True:
    n = int(input(":::"))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if cont == 1:
        menor = n
    elif n < menor:
        menor = n
    r = input("Deseja continuar? ")
    if r in 'Nn':
        break

media = soma/cont
print(media)
print(maior)
print(menor)
