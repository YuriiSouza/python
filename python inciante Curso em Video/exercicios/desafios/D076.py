# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tupla = ['Carne', 22, 'Arroz', 10, 'feijão', 4, 'Tomate', 3]

for n in range(0, 8, 2):
    print(f"{tupla[n]} .... R$ {tupla[n+1]},00")
