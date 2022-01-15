#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos degitos separados.
#Ex: número 1834 unidade:4  dezena:3  centena:8  milhar:1

#Solução matemática:

num = int(input("Digite um numero de 0 a 9999: "))

milhar = int(num/1000)
centena = int((num - (milhar * 1000))/100)
dezena = int((num - (centena * 100 + milhar * 1000))/10)
unidade = (num - (dezena*10 + centena * 100 + milhar * 1000))
'''
milhar = num // 1000 % 10
centena = num //100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10
'''

print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))
