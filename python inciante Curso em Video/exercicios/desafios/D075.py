# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

tupla = int(input("Valor: ")), int(input("Valor: ")), int(input("Valor: ")), int(input("Valor: "))

c = cont9 = 0
while c < 4:
    if tupla[c] == 9:
        cont9 += 1
    c += 1

if cont9 > 0:
    print(f"Apareceram {cont9} noves...")
else:
    print("Não apareceu nove...")

if tupla.index(3) >= 0:
    print(f"O 3 foi o {tupla.index(3) + 1} número a ser digitado.")
else:
    print("O valor 3 não foi digitado.")

print("Os números pares: ")

c = quantPar =  0
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end = ', ')
        quantPar += 1
if quantPar == 0:
    print(f"Não foram digitados números pares.")
