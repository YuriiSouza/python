numeros = []

for i in range(0, 3):
    numeros.append(int(input("Numero: ")))
    
    
numeros = sorted(numeros, reverse = True)

for i in range(0, 3):
    print(numeros[i])
    