#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

List = []
princ = []

while True:
    List.append(str(input("Name: ")))
    List.append(int(input("Weight: ")))
    princ.append(List[:])
    List.clear
    
    validation = str(input("Do you wanna continue? "))
    if validation in 'Nn':
        break


print("")
print(f"Number of peoples inserts is {len(princ)}\n")
print(f"\nThe ligthers is the:")
for n in range(0, len(princ)):
    if princ[n][2] < 70:
        print(princ[n][], end = ' ')
    print(f"The  weight", lighter[n])
print(f"\nThe fatters is: ")
for n in range(0, len(mostWeightName)):
    print(mostWeightName[n])
    print(f"Your weight is {mostWeight[n]}")
