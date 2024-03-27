medias = []
soma_nota_ciclo = 0
media_do_ciclo = 0
pesos = []
soma_de_pesos = 0


while True:
    print("A soma dos pesos deve totalizar 10.")
    
    for j in range(0, 4):#peso de cada nota
        while True:
            try:
                peso = float(input(f"Peso da nota {j+1}: "))
            
                if peso == int(peso):
                    pesos.append(peso)
                    break
                
            except:
                pass
                
    for p in pesos:
        soma_de_pesos += p 
        
    if soma_de_pesos == 10:
        break
    else:
        print("Pesos inválidos", end="\n")
        pesos.clear()
        soma_de_pesos = 0
            

for i in range(0, 3):#ciclos
    print(f"::::::Ciclo {i + 1}::::::")
    for j in range(0, 4):#notas de um ciclo
        while True:
            try:
                nota = float(input(f"Nota{j+1}: "))
                if nota <=10 and nota >=0:
                    break
        
            except:
                pass
            
        
        soma_nota_ciclo += (nota * pesos[j])/10
        
    medias.append(soma_nota_ciclo)
    soma_nota_ciclo = 0
    
    
soma_medias_ciclo = 0
media_semestre = 0

# print(medias)
for n in medias:
    soma_medias_ciclo += n
    
    media_semestre= soma_medias_ciclo / 3
    
print(f"Média: {media_semestre}")
