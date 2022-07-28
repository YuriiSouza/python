#Faça um programa que leia os dias e a quilometragem de um carro alugado e calcule o valor a ser pago pelo aluguel, sendo que, cada dia custa R$60,00 e R$0,15 reais cada km.
nDias = int(input("Quantidade de dias que você ficou com o carro:"))
nKm = float(input("Quantidade de KM rodados: "))

valor = (nDias * 60) + (nKm * 0.15);

print("O valor gasto com o carro alugado foi de R${:.2f}".format(valor))
