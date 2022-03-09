# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 
contMaior18 = 0
contM = 0
while True:
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    while True:
        sexo = str(input("Sexo"))
        if sexo in "MnFf":
            break
        else:
            print("Valor invalido...")
    if idade > 18:
        contMaior18 += 1
    if sexo in "Mm":
        contM += 1
    
    while True:
        condicao = str(input("Deseja continuar? [S/N]"))
        if condicao in "NnSs":
            break
    if condicao in "nN":
        break