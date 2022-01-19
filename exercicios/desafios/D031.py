#Desenvolva um programa que pergunte a distâcia de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distância = float(input("Qual a distância da viagem? "))

if distância <= 200:
    valor = distância*0.5;
else:
    valor = distância*0.4;

print("O valor da viagem será de {:.2f}".format(valor))
