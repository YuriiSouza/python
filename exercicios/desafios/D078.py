# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
listaNumerica = []

for n in range(0, 5):
    j = int(input("Digite o valor: "))
    listaNumerica.append(j)
    
print("")

print("VALORES", end = ":::")
print(listaNumerica)

print(f"O valor menor {min(listaNumerica)} esta nas posições: ", end = "")
for n, i in enumerate(listaNumerica):
    if i == min(listaNumerica):
        print(f"{n + 1} ...", end = "...")

print(f"\nO valor maior {max(listaNumerica)} está nas posições: ", end = "")

for n, i in enumerate(listaNumerica):
    if i == max(listaNumerica):
        print(f"{n + 1} ..." , end = "")
