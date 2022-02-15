#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
mulheresmenosde20 = 0
for i in range(0,4):
    while True:
        nome = str(input("Nome: "))
        if (nome != '') and (type(nome) == str):
            break
    
    idade = int(input("Idade: "))

    while True:
        sexo = str(input("Sexo: ")).lower()
        if (sexo != '') and (type(sexo) == str) and (sexo == 'masculino' or sexo == 'feminino'):
            break

    idadetotal =+ int(idade);
    
    if (i == 0) and (sexo == 'masculino'):
        maisvelho = nome;
        maisidademasculino = idade;
    elif (sexo == 'masculino') and (idade > maisidademasculino):
        maisvelho = nome;
        maisidademasculino = idade;

    if (sexo == 'feminino') and (idade < 20):
        mulheresmenosde20 = mulheresmenosde20 + 1;

mediaidade = idadetotal/4

print(f'''A média de idade do grupo é {mediaidade}
O nome do homen mais velho é {maisvelho}
Existem {mulheresmenosde20} com menos de 20 anos. ''')
