lado1 = int(input("Lado 1:"))
lado2 = int(input("Lado 2:"))
lado3 = int(input("Lado 3:"))

n1 = lado1 + lado2
n2 = lado2 + lado3
n3 = lado3 + lado1

if n1 > lado3 and n2 > lado1 and n3 > lado2:
    if lado1 == lado2 and lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Isóceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo")
    