#Faça um programa que leia as medidas de uma parede e calcule a quantidade de tinta nescessaria para pinta-la, sendo que 2 metros quadrados de parede precisam de 1 litro de tinta para ser pintado
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

área = largura*altura;
litrosDeTinta = área/2;

print("A parede tem {} metros quadrados.\nPrecisa de {} litros de tinta para ser completamente pintada.".format(área, litrosDeTinta))
