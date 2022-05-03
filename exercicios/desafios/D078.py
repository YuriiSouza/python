# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
listaNumerica = []
listmaior = []
listmenor = []

for n in range(0, 5):
    j = int(input("Digite o valor: "))
    listaNumerica.append(j)
    
for n in listaNumerica:
    if n == max(listaNumerica):
        listmaior.append(listaNumerica.index)
    if n == min(listaNumerica):
        listmenor.append(listaNumerica.index)

print("VALORES", end = ":::")
print(listaNumerica)

print(f"O valor menor {min(listaNumerica)} esta nas posições: ", end = "")
for n, i in enumerate(listmenor):
    print(i, "...", end = " ")

print(f"O valor maior {max(listaNumerica)}")
