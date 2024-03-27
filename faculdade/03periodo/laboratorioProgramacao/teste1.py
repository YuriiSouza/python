# def calcular_soma(n):
#     soma = 0
#     for i in range(1, n+2):
#         numerador = i**2 + 1
#         denominador = i + 3
#         parcela = numerador / denominador
#         print(parcela)
#         soma += parcela
#     return soma


# resultado = calcular_soma(5)
# print("O resultado ", resultado)

# def calcular_soma(n):
#     soma = 0
#     for i in range(1, n + 1):
#         numerador = i**2 + 1
#         denominador = i + 3
#         parcela = numerador / denominador
#         soma += parcela
#     return soma

# resultado = calcular_soma(-3)
# print("teste", resultado)

# def argu(num):
#     if num == 0:
#         return 0
#     else:
#         print(num%2, num//2)
#         return (num % 2) + 10 * argu(num//2)
    
# print(argu(5))

def resur(x):
    if x == 1:
        return -x
    else:
        
        return -5 * resur(x - 1) + x

print(resur(4))
