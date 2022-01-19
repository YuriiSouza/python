#Faça um programa que leia um ano e retorne se ele é bissesto.
from datetime import date
ano = int(input("Ano: "))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print("{} é um ano bissesto.".format(ano))
else:
    print("{} não é um ano bissesto.".format(ano))
