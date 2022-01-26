#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiroTermo = float(input("Primeiro termo: "))
razao = float(input("Razão: "))

for c in range(0, 10):
    print(primeiroTermo)
    primeiroTermo += razao;
