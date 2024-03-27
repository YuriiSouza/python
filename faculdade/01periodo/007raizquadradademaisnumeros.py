numeros = []
maior = 0

quant_numeros = int(input("quantos numeros ira digitar: "))

for n in range(0, quant_numeros):
    numeros.append(float(input("Adcine o número: ")))
    
    
for n in numeros:
    if n > maior:
        maior = n
    else:
        maior = maior
    
print(f"Maior = {maior}")
