#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

from turtle import clear

totIdade = media = 0
mulheres = list()
lista = list()
acimadamedia = list()
dados = dict()

while True:
    dados['nome'] = str(input("Nome: "))
    
    while True:    
        dados['sexo'] = str(input("Sexo[F/M]: ")).lower()
        if dados['sexo'] in 'fm':
            break
        else:
            print("Apenas F ou M, por favor.")

    while True:
        try:
            dados['idade'] = int(input("Idade: "))   
            break 
        except:
            print("Dados invalidos")
    
    lista.append(dados.copy())
    dados.clear()

    while True:
        validacao = str(input("Deseja continuar? [S/N]  ")).lower()
        if validacao in 'sn':
            break
        else:
            print("Valor invalido...")

    if validacao in 'n':
        break

for n in lista:
    totIdade = totIdade + n['idade']
    if n['sexo'] == 'f':
        mulheres.append(n['nome'])
media = totIdade/len(lista)

for n in lista:
    if n['idade'] >= media:
        acimadamedia.append(n['nome'])

print("=-"*10)
print(f"Pessoas cadastradas: {len(lista)}")
print("=-"*10)
print(f"Media de Idade: {media}")
print("=-"*10)
print("Mulheres inseridas: ")
for n in mulheres:
    print(f"  ==> {n}")
print("=-"*10)
print("Pessoas acima da media de idade: ")
for n in acimadamedia:
    print(f"  ==> {n}")
print("=-"*10)
