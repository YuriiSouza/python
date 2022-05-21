#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(c, l, m):
    print(f"Area = {(c * l):.2f} {m} quadrados")


#Programa principal...
while True:        
    medida = str(input("Qual a medida: "))
    if medida not in "":
        break

while True:    
    try:
        comprimento = float(input("Comprimento: "))
        break
    except:
        print("ERRO")

while True:
    try:
        largura = float(input("Largura: "))
        break
    except:
        print("ERRO")

area(comprimento, largura, medida)
