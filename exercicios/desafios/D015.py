nDias = int(input("Quantidade de dias que você ficou com o carro:"))
nKm = float(input("Quantidade de KM rodados: "))

valor = (nDias * 60) + (nKm * 0.15);

print("O valor gasto com o carro alugado foi de R${:.2f}".format(valor))
