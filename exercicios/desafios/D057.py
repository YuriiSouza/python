# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
nome = str(input("Nome: "))
while True:
    sexo = str(input("Sexo m/f: ")).lower()
    if sexo == 'm' or sexo == 'f':
        break
