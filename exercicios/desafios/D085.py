#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

x = y = 0
generalList = [[],[]]

#In this list, i will append all the values, all separate in a matrix

for n in range(0,7):
    number = int(input("Value = "))
    
    if number % 2 == 0:
        generalList[0].append(number)
    else:
        generalList[1].append(number)


generalList[0].sort()
generalList[1].sort()
print(f"The pair numbers is {generalList[0]}")
print(f"The odd numbers is {generalList[1]}")
