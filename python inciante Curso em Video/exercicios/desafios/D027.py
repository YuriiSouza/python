#Faça um programa que leia um nome e retorne o primeiro e o ultimo.
nome = str(input("Digite seu nome completo: ")).sprit()
cadaNome = nome.split()

print("Primeiro nome: {}".format(cadaNome[0]))
print("Ultimo nome: {}".format(cadaNome[len(cadaNome)-1]))