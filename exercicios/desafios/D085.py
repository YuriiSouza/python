#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

x = y = 0
generalListodd = list()
generalListpair = list()

#In this list, i will append all the values, all separate in a matrix

for n in range(0,7):
    number = int(input("Value = "))
    
    if number % 2 == 0:
        generalListodd.append(number)
    else:
        generalListpair.append(number)


print(f"odd = {generalListodd}")
print(f"pair = {generalListpair}")
