#Faça um program que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

menor = 0;
maior = 0;

if n1 > n2:
    maior = n1
else:
    maior = n2