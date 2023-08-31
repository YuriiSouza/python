from math import sqrt

lado1 = int(input("Lado 1 em m:"))
lado2 = int(input("Lado 2 em m:"))
lado3 = int(input("Lado 3 em m:"))


n1 = lado1 + lado2
n2 = lado2 + lado3
n3 = lado3 + lado1

if n1 > lado3 and n2 > lado1 and n3 > lado2:
    p = (lado1 + lado2 + lado3)/2 #semiperimetro

    a = sqrt(p * (p - lado1)*(p - lado2)*(p - lado3)) #area

    print(f"A area desse triângulo é : {a} metros quadrados")
else:
    print("Não é um triângulo")
