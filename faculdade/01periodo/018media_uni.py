medias = []
soma_nota_ciclo = 0
media_do_ciclo = 0

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
            
        
        soma_nota_ciclo += nota
        
    media_do_ciclo = soma_nota_ciclo / 4
    
    soma_nota_ciclo = 0
    
    medias.append(media_do_ciclo)
    
soma_medias_ciclo = 0
media_semestre = 0

for n in medias:
    soma_medias_ciclo += n
    
    media_semestre= soma_medias_ciclo / 3
    
print(f"Média: {media_semestre}")
