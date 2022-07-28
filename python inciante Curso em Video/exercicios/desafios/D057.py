# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
nome = str(input("Nome: "))
sexo = str(input("Sexo m/f: ")).strip().lower()[0]
while sexo not in "MmFf":
    sexo = str(input("Resultado inválido, por favor, digite seu sexo: ")).strip().lower()[0]
