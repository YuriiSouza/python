#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia():
    lista = list()
    print("Valores sorteados: ")
    for n in range(0, 5):
        r = randint(0, 10)
        lista.append(r)
        print(r, end = " ")
        sleep(0.75)
    return lista

def somaPar(x):
    somapar = 0
    for n in x:
        if n % 2 == 0:
            somapar += n
    return somapar

numeros = list()
numeros = sorteia()    

print(" ")
print("=-" * 20)
print("Os valores pares são: ")

cont = 0
for n in numeros:
    if n % 2 == 0:
        print(n)
        cont += 1
if cont == 0:
    print("Não existe valores pares...")

print(f"A soma é {somaPar(numeros)}")
