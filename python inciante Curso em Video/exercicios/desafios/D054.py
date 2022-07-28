#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
nome = ['','','','','','','']
idade = [0,0,0,0,0,0,0]
maiorDeIdade = [False,False,False,False,False,False,False]
quantMaior = 0
quantMenor = 0
for c in range(0, 7):
    nome[c] = str(input("Nome: "))
    idade[c] = date.today().year - int(input("Qual ano você nasceu: "))
    print("-="*10)
    if idade[c] >= 18:
        maiorDeIdade[c] = True
        quantMaior += 1
    else:
        maiorDeIdade[c] = False
        quantMenor += 1
    
for c in range(0, 7):
    print(f"O {nome[c]} tem {idade[c]}\n Maior de idade? {maiorDeIdade[c]}\n\n")

print(f"Temos {quantMaior} maiores de idade e {quantMenor} menores de idade...")