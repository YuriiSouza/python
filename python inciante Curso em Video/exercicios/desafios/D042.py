#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print("-="*20)
print("ANALISANDO TRIÂNGULOS")
print("-="*20)

lado1 = float(input("Lado do triângulo: "))
lado2 = float(input("Lado 2 do triânglo: "))
lado3 = float(input("Lado 3 do triângulo: "))
 
menor = lado1
maior = lado1

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 +lado1 > lado2:
    print("\nOs lados podem formar um triângulo...")
    if lado1 == lado2 == lado3:
        print("Triângulo EQUILÁTERO.")
    elif lado1 != lado2 != lado3 != lado1:
        print("Triângulo ESCALENO.")
    else:
        print("Triângulo ISÓCELES.")
else:
    print("Os lados não formam um triângulo...")

print("="*40)
