#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
list1 = list()
listJustPair = list()
listJustOdd = list()

while True:
    n = int(input("Número: "))

    list1.append(n)

    if n % 2 == 0:
        listJustPair.append(n)
    else:
        listJustOdd.append(n)

    verification = str(input("Do you wanna stop? [Y/N]: "))
    if verification in 'Yy':
        break;

print(f"The numbers insited: {list1}")
print(f"The paur numbers is {listJustPair}")
print(f"The paur numbers is {listJustOdd}")
