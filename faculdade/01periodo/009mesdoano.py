meses_do_ano = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

while True:
    mes = int(input("Digite um numero de 1 a 12: "))
    
    if mes > 0 and mes < 13:
        break
    
mes_ano = meses_do_ano[mes]

print(mes_ano)
