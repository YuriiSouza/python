#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

list1 = list()
allList = list()

while True:
    list1.clear()
    list1.append(str(input("Name: ")).lower())
    list1.append(float(input("Resulted 1: ")))
    list1.append(float(input("Resulted 2: ")))

    allList.append(list1[:])

    question = str(input("Do you continue?\n ")).lower()
    if question in 'no':
        break

for x in range(0, len(allList)):
    print("")
    print("=-"*10)
    print(f"Name: {allList[x][0]}")
    print(f"1 -> {allList[x][1]}")
    print(f"2 -> {allList[x][2]}")
    print("=-"*10)
    print("")

verification = str(input("Do you wanna see the results of someone? ")).lower()
if verification in 'y':
    while True:    
        name = str(input("Name: "))
        for x in range(0, len(allList)):
            if allList[x][0] == name:

                media = (allList[x][1] + allList[x][2]) / 2

                print("")
                print("=-"*10)
                print(f"Name: {allList[x][0]}")
                print(f"1 -> {allList[x][1]}")
                print(f"2 -> {allList[x][2]}")
                print(f"The MEDIA: {media}")
                print("=-"*10)
                print("")
        verify = str(input("Do you wanna see the results of someone? ")).lower()
        if verify in 'no':
            break

else:
    print("GOOD BYE")

print("GOOD BYE")
