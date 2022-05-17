# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = dict()

dados['nome'] = str(input('Name: '))
year = int(input('Year of birth: '))
dados["years"] = date.today().year - year
dados['work card'] = int(input("Number of work card: "))
if dados['work card'] > 0:
    dados['Year od contratation'] = int(input("Year od contratation: "))
    dados['wage'] = ("R$") + str(input('Wage: '))
    dados['retiriment'] = dados['years'] + (35 - (date.today().year - dados['Year od contratation']))

print("=-" * 15)
for n, y in dados.items():
    print(f"{n} has the value {y}")
    