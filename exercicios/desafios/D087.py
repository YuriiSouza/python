#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matrix = [[], [], []]
pair = 0
thirtcolumn = 0
bigger = 0

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line].append(int(input(f"Value of line {line} and column {column}::: ")))

        if column == 2:
            thirtcolumn += matrix[line][2]

for line in range(0, 3):
    for column in range(0, 3):        
        if matrix[line][column] % 2 == 0:
            pair = pair + matrix[line][column]

for n in range(0, 3):
    if n == 0:
        bigger = matrix[1][n]
    else:
        if bigger < matrix[1][n]:
            bigger = matrix[1][n]

for line in range(0, 3):
    print(" ")
    for column in range(0, 3):
        if matrix[line][column] % 2 == 0:
            print(f"[={matrix[line][column]}=]", end = " ")
        else:
            print(f"[{matrix[line][column]}]", end = " ")

print("Os valores pares: ", pair)

print("Soma da terceira coluna", thirtcolumn)

print("O maior valora da segunda linha é", bigger)
