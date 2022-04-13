#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
names = list()
weight = list()
mostWeight = list()
lighter = list()
mostWeightName = list()
lighterName = list()

while True:
    name = str(input("Insert name: "))
    weight1 = int(input("Insert the weight: "))
    names.append(name)
    weight.append(weight1)
    
    if weight1 > 70:
        mostWeightName.append(name)
        mostWeight.append(weight1)
    else:
        lighterName.append(name)
        lighter.append(weight1)

    verification = str(input("Do you wanna continue[Y/N]: "))
    if verification in 'Nn':
        break;


print("")
print(f"Number of peoples inserts is {len(names)}\n")
print(f"\nThe ligthers is the:")
for n in range(0, len(lighterName)):
    print(lighterName[n], end = ' ')
    print(f"The  weight", lighter[n])
print(f"\nThe fatters is: ")
for n in range(0, len(mostWeightName)):
    print(mostWeightName[n])
    print(f"Your weight is {mostWeight[n]}")
