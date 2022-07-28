#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(n):
    maior1 = cont = 0
    for x in n:
        if cont == 0:
            maior1 = x
        if maior1 < x:
            maior1 = x
        cont += 1
    print(maior1)



list1 = list()
while True:
    n = int(input("Insira: "))
    list1.append(n)

    while True:
        confirmação = str(input("Deseja inserir mais numero? ")).lower()[0]
        if confirmação in 'sn':
            break

    if confirmação == 'n':
        break

print("-=" * 20)
print(f"O maior valor dos valores {list1}")
maior(list1) 
