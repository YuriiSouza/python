# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matrix = [[],[],[]]
for line in range(0, 3):
    for column in range(0, 3):
        number = int(input(f"Number of line {line + 1} and column {column + 1}: "))
        matrix[line].append(number)
for line in range(0, 3):
    print(" ")
    for column in range(0, 3):
        print(f"[{matrix[line][column]:^5}]", end = " ")
