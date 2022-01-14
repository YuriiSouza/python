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
#Solução str
'''
numero = str(input("Digite um número de 0 a 9999: "))
print(len(numero)-1)
print(len(numero)-2)
print(len(numero)-3)
print(len(numero)-4)

print("Unidade: {}".format(numero[len(numero)-1]))
print("Dezena: {}".format(numero[abs(len(numero)-2)]))
print("Centena: {}".format(numero[abs(len(numero)-3)]))
print("Milhar: {}".format(numero[abs(len(numero)-4)]))
'''
