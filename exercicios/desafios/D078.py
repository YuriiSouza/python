# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
listaNumerica = [list]

for n in range(0, 5):
    j = int(input("Digite o valor: "))
    listaNumerica.append(j)
    if n == 0:
        menor = j
        maior = j
    elif menor > j:
        menor = j
    elif maior < j:
        maior = j
    
print(listaNumerica)
print(f"{maior} é o maior termo e esta na posição {listaNumerica.index(maior)}\n{menor} é o menor valor na posição {listaNumerica.index(menor)}")
