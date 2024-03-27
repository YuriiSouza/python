def ver_multiplos(numero):
    for index, n in enumerate(numero):
        divisores = []
        
        for i in range(index+1, len(numero)):
            divisao = numero[index] % numero[i]
            
            if  divisao ==  int(divisao):
                divisores.append(numero[i])
                
        print(f"{numero[index]} e multiplo de {divisores}")

numero = []    

for n in range(0, 3):
    n1 = int(input("Numero:"))
    numero.append(n1)

numero = sorted(numero, reverse = True)
print(numero)

ver_multiplos(numero)

    