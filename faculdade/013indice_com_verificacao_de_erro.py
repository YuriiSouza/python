#numero 5
from time import sleep

cont = 0
while True:
    while True:
        indice_de_gravidade = int(input("Nível de risco: "))

        if indice_de_gravidade > 0 and indice_de_gravidade <= 10:
            break
    
    if indice_de_gravidade > 9:
        print("Grave")
        cont = cont + 1
        sleep(1)
    else:
        print(".")
        sleep(1)
        
    if cont >= 3:
        print("explodiu")
        sleep(2)
        break
    