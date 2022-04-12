#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
list = list()

while True:
    number = int(input("number: "))
    list.append(number)
    verification = input("Do you wanna continue? [Y/N] ")
    if verification in 'Nn':
        break

print(f"The total number of number entered was {len(list)}")
list.sort(reverse = True)
print(list)

if 5 in list:
    print("The number 5 is on the list...")
else:
    print("The list don't contain the number 5...")
