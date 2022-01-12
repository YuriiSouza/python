#Salário com 15% de aumento
salário = float(input("Digíte o valor atual do salário: "))

salárioFinal = salário + (salário*0.15);

print("Tendo R${:.2f} de salário, com 15%' de aumento tera um salário de R${:.2f}.".format(salário, salárioFinal))
