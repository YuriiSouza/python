#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = [list]

while True:
    valor = int(input("Valor: "))
    if valor not in valores:
        valores.append(valor)

    continua = str(input("Deseja continuar? "))
    if continua in 'Nn':
        break

cont = menor = 0
valoresOrdenado = [list]
while cont < len(valores):
    if cont == 0:
        menor == valores[cont]
    elif 