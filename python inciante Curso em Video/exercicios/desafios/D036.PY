#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print("-="*7,"Financiamento","-="*7)
valorCasa = float(input("Valor da casa: "))
salario = float(input("Sálario: "))
tempo = int(input("Tempo que deseja parcelar(anos): "))*12

parcela = valorCasa/tempo;

if salario >= parcela*0.3:
    print("Parabéns, você pode fazer nosso financiamento")
    print("Parcela mensal: R${:.2f}".format(parcela))
else:
    print("Financiamento negado...")