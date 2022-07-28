#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint


tupla = randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999), randint(0, 9999)

for n in range(0, 5):
    if n == 0:
        menor = tupla[0]
        maior = tupla[0]
    elif menor > tupla[n]:
        menor = tupla[n]
    elif maior < tupla[n]:
        maior = tupla[n]

print(f"Entre {tupla}")
print(f"MAIOR ==> {maior}")
print(f"MENOR ==> {menor}")
