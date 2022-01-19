#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se ekas podem ou não formar um triângulo.
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
else:
    print("Os lados não formam um triângulo...")

print("="*40)
