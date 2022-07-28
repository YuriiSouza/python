#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dados = dict()

dados['Name'] = str(input("What's that name? "))
dados['Avarege'] = float(input("What's the avarage "))
if dados['Avarege'] >= 6.0:
    dados['Situation'] = 'Approved'
else:
    dados['Situation'] = 'Desapproved'

for x, y in dados.items():
    print(f"{x} = {y}")
