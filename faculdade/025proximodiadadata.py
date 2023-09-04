def ano_bissexto(ano):
    bissexto = bool
    
    if ano % 4 == 0 and ano % 100 != 0:
        bissexto = True
        
    elif ano % 4 != 0 and ano % 400 != 0 : 
        bissexto = False
        
    elif ano % 4 != 0 and ano % 400 == 0:
        bissexto = True
    
    return bissexto #retorna um valor bool, sé ou não bissexto



if ano_bissexto(n):
    print("sim")
else:
    print("nao")
    