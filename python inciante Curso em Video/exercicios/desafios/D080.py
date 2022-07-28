#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()

maior = c = 0
for n in range(0, 5):
    valor = int(input(f"Valor {n}: "))
    
    if n == 0 or valor > valores[len(valores)-1]:
        valores.append(valor)
        print(f"Inserido na ultima posição.")
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break;
            pos += 1

        print(f"Esta na posição {pos + 1}")

print(valores)
