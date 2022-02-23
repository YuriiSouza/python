#Faça um programa que leia um número qualquer e mostre o seu fatorial.
print("-="*10)
print("FATORIAL")
print("-="*10)
while True:
    fatorial = 1
    n = int(input("Digite um número: "))
    for i in range(1,n+1):
        if i == n:
            print(i)
        else:
            print(i, "x", end=" ")        
        fatorial = fatorial * i
    print(f"{n}! = {fatorial}")
    v = str(input("Deseja inserir outro valor? ")).strip()[0]
    if v in "Nn":
        break
