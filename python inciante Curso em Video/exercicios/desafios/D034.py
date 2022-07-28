#Escreva um programa que calcule o salário do funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Salário: "))

if salario >= 1250:
    salarioAjustado = salario + (salario * 0.10);
else:
    salarioAjustado = salario + (salario*0.15);

print("O novo valor do salário será de R${:.2f}".format(salarioAjustado))
