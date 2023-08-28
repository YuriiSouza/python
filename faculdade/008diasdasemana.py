dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

while True:
    dia = int(input("Digite um numero de 1 a 7: "))
    
    if dia > 0 and dia < 8:
        break
    
dia_semana = dias_da_semana[dia]

print(dia_semana)
