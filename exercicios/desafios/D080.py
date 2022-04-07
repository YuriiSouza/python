#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()

maior = c = 0
for n in range(0, 5):
    valor = int(input(f"Valor {n}: "))
    if n == 0:
        valores.append(valor)
    elif valor > valores[len(valores)-1]:
        valores.append(valor)
    else:
        if valor < valores[len(valores)-1]:
            maior = valores[len(valores)-1]
            del valores[len(valores)-1]
            valores.append(valor)
            valores.append(maior)
            if valores[len(valores)-]