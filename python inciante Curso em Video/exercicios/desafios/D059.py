#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from lib2to3.pgen2.grammar import opmap_raw


n1 = int(input("N1 = "))
n2 = int(input("N2 = "))

while True:
    operacao = int(input("""
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA 
    """))

    if operacao == 1:
        resultado = n1 + n2;
        print(f"{n1} + {n2} = {resultado}")
    elif operacao == 2:
        resultado = n1 * n2;
        print(f"{n1} x {n2} = {resultado}")
    elif operacao == 3:
        if n1 > n2:
            resultado = n1;
        else:
            resultado = n2;
        print(f"O maior número é {resultado}")
    elif operacao == 4:
        n1 = int(input("N1 = "))
        n2 = int(input("N2 = "))
    elif operacao == 5:
        break
