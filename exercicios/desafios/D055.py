#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
for i in range(0, 5):
    p = int(input(print("Digíte o seu peso: ")))
    
    if i == 0:
        maior = p
        menor = p
    elif p > maior:
        maior = p
    elif p < menor:
        menor = p

print(f"""O maior peso é {maior}
O menor valor é {menor}""")
