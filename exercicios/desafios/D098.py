#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada#
from turtle import clear


def contador(inicio, fim, passo):
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}")
    cont = inicio
    
    if passo < 0:
        passo = passo * (-1)
    if fim > inicio:
        while fim > cont:
            print(cont)
            cont += passo
    if fim < inicio:
        while fim < cont:
            print(cont)
            cont -= passo



#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

contador(i, f, p)
