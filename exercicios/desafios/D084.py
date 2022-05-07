#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

from this import d


List = []
princ = []
mai = men = 0

while True:
    List.append(str(input("Name: ")))
    List.append(int(input("Weight: ")))
    if len(princ) == 0:
        mai = men = 0
    else:
        if mai < List[1]:
            mai = List[1]
        elif men > List[1]:
            men = List[1]

    princ.append(List[:])
    List.clear
    
    validation = str(input("Do you wanna continue? "))
    if validation in 'Nn':
        break


print("")
print(f"Number of peoples inserts is {len(princ) + 1}\n")

print(f"O wegihter is {mai}")
print(f"The ligthest is {men}")