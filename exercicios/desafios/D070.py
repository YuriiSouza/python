# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
Total = 0
cont1000 = 0
menorNome = ""
menorPreco = 0
while True:
    nome = str(input("Nome: "))
    preco = float(input("Preço: R$"))
    
    Total += preco
    
    if preco > 1000:
        cont1000 += 1
    
    if menorPreco == 0:
        menorNome = nome
        menorPreco = preco
    elif menorPreco > preco:
        menorNome = nome
        menorPreco = preco
    
    while True:
        cond = str(input("Deseja continuar? [S/N]"))
        if cond in "SsNn":
            break
    if cond in "Nn":
        break

print(f"Total: R${Total:0.2f}\nProdutos com preço superior à R$1000,00:{cont1000}\nProduto mais barato: {menorNome} valendo R${menorPreco:0.2f}")