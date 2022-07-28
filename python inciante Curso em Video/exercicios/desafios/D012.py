#Faça um programa que leia o valor de um produto e desconto a ele dado e retorne o valor final.
valorDoProduto = float(input("Valor do produto: "))
desconto = float(input("Valor do desconto(em porcentagem): "))

valorFinal = valorDoProduto - (valorDoProduto *(desconto / 100.0));

print("O produto com desconto de {:1f}% é: {:.2f}".format(desconto, valorFinal))
