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
mes = int(data[1])
ano = int(data[2])

if mes == 1:
    mes_anterior = meses[11]
else:
    if dia == 1:
        mes_anterior = meses[mes - 1]
    mes_anterior = meses[mes - 1]
    
quant_dias_no_mes_anterior = quant_dias_mes(mes-1, bissexto)
if dia == 1:
    dia_anterior = quant_dias_no_mes_anterior
else:
    dia_anterior = dia - 1


if mes == 1 and dia == 1:
    ano_anterior = ano - 1
else:
    ano_anterior = ano

print(f'O dia anterior é: {dia_anterior} de {mes_anterior} de {ano_anterior}')
