#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".

n = str(input("Digite um nome: ")).strip()


nomeRepartido = n.split()

print("O nome recebe com 'santo'? ")
print(nomeRepartido[0] == 'santo')