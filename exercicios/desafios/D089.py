#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

list1 = list()

while True:
    name = str(input("Name: ")).lower()
    n1 = float(input("Resulted 1: "))
    n2 = float(input("Resulted 2: "))
    media = (n1 + n2) / 2

    list1.append([name, [n1, n2], media])

    question = str(input("Do you continue?\n ")).lower()
    if question in 'no':
        break

print(f'{"number ":<4}{"Name":<10}{"Avarege":>8}')
for x, y in enumerate(list1):
    print(f'{x:<5} {y[0]:<10}{y[2]:>8}')



verification = str(input("Do you wanna see the results of someone? ")).lower()
if verification in 'y':
    while True:    
        name = str(input("Name: "))
        for y in list1:
            if y[0] == name:
                print(f"Name: {y[0]}\nAvarege: {y[2]}")
            

        verify = str(input("Do you wanna see the results of someone? ")).lower()
        if verify in 'no':
            break

else:
    print("GOOD BYE")

print("GOOD BYE")
