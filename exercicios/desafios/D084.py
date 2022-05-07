#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

List = []
princ = []
mai = 0
men = 0

while True:
    List.append(str(input("Name: ")))
    List.append(int(input("Weight: ")))
    if len(princ) == 0:
        mai = men = List[1]
    else:
        if men > List[1]:
            men = List[1]
        if mai < List[1]:
            mai = List[1]
        

    princ.append(List[:])
    List.clear
    
    validation = str(input("Do you wanna continue? "))
    if validation in 'Nn':
        break


print("")
print(f"Number of peoples inserts is {len(princ)}\n")

print(f"O wegihter is {mai}")
for n in princ:
    if n[1] == mai:
        print(n[0])
print(f"The ligthest is {men}")
for n in princ:
    if n[1] == men:
        print(n[0])
