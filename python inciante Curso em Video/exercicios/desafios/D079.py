#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()

while True:
    valor = int(input("Valor: "))
    if valor not in valores:
        valores.append(valor)
        print("Valor adcionado com sucesso...")
    else:
        print("Valor ja digitado.")
    while True:
        continua = str(input("Deseja continuar? "))
        if continua in 'SsNn':
            break
        else:
            print("Valor invalido...")
    if continua in 'Nn':
        break

#cont = menor = cont1 = 0
valoresOrdenado = list()

'''while cont < len(valores):
    while cont1 < len(valores):
        if cont1 == 0:
            menor == valores[cont1]
        elif menor > valores[cont1]:
            menor = valores[cont1]
        cont1 = cont1 + 1
    valores.append(menor)
    cont = cont + 1
'''
menor = 0
for cont in range(0, len(valores)):
    for cont1 in range(0, len(valores)):
        if cont1 == 0:
            menor = valores[cont1]
        elif menor > valores[cont1]:
            menor = valores[cont1]
    valoresOrdenado.append(menor)
    valores.remove(menor)
print(valores)
print(valoresOrdenado)
