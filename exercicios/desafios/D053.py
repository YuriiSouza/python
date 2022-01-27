#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input("Digite uma frase para analise: ")).lower().split()
frase1 = ''

for c in range(0,len(frase)):
    frase1 = frase1 + frase[c]

y = len(frase1) - 1

for c in range(0, len(frase1)):
    if frase1[c] == frase1[y - c]:
        continue
    else:
        print("Não é um palíndromo.")
        break

print("A frase é um palíndromo!!!")