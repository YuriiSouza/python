#Escreva um program que leia a velocidade de um carro.
#Se ele ultrapassar 80 Km/h. Mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("Velocidade do carro: "))

if velocidade > 80:
    print("MULTADO")
    valor = (velocidade - 80)*7;
    print("O valor da multa é de R${:.2f}".format(valor))
else:
    print("Não multado")
