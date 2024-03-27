def ano_bissexto(ano):
    bissexto = bool
    
    if ano % 4 == 0 and ano % 100 != 0:
        bissexto = True
        
    elif ano % 4 != 0 and ano % 400 != 0 : 
        bissexto = False
        
    elif ano % 4 != 0 and ano % 400 == 0:
        bissexto = True
    
    return bissexto #retorna um valor bool, sé ou não bissexto

def quant_dias_mes(mes_numero, bissexto):
    if bissexto:
        meses = [31,29,31, 30, 31,30, 31,31, 30,31, 30,31]
    else:
        meses = [31,28,31, 30, 31,30, 31,31, 30,31, 30,31]
        
    return meses[mes_numero - 1]
       
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

while True:
    try:
        data = input("data: ")
        
        if data[2] == '/' and data[5] == '/':#conferindo a formatação
            data = data.split('/')#separando dia mes e ano em uma lista
            
            bissexto = ano_bissexto(int(data[2]))
            
            if int(data[1]) > 0 and int(data[1]) < 13: #verificando se o mes esta no limite certo
                quant_dias_no_mes = quant_dias_mes(int(data[1]), bissexto)#conferindo quantidade de dias do mes escolhido
                if int(data[0]) > 0 and int(data[0]) <= quant_dias_no_mes:#verificando se os dias estao dentro do prazo do mes
                    break
                else:
                    print("Quantidade de dias incompatível com o mês")
            else:
                print("mês não existe")
        else:
            print("formatação: xx/xx/xxxx")
    except:
        print("erro")

dia = int(data[0])
if dia == quant_dias_no_mes:
    dia_seguinte = 1
else:
    dia_seguinte = dia + 1

mes = int(data[1]) - 1
if mes == 11:
    mes_seguinte = meses[0]
else:
    if dia == quant_dias_no_mes:
        mes_seguinte = meses[mes + 1]
    else:
        mes_seguinte = meses[mes]
    

ano = int(data[2])
if mes == 11 and dia == quant_dias_no_mes:
    ano_seguinte = ano + 1
else:
    ano_seguinte = ano

print(f'O proximo dia é: {dia_seguinte} de {mes_seguinte} de {ano_seguinte}')
