#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()

maior = 0
for n in range(0, 5):
    valor = int(input(f"Valor {n}: "))
    if n == 0:
        valores.append(valor)
    '''for cont in range(len[valores], -1, -1):
        if valor > valores[len(valores)-cont]:
            valores.append(valor)
        elif valores[len(valores)-cont] > valor:
            maior = valores[len(valores)-cont]
            del valores[len(valores)-cont]
            valores.append(valor)
            valores.append(maior)'''
    

    if valor > valores[len(valores)-1]:
        valores.append(valor)
    for cont in range(len(valores)-1, -1, -1):
        if valores[cont] > valor:
            maior = valores[cont]
            del valores[cont]
            valores.append(valor)
            valores.append(maior)

print(valores)