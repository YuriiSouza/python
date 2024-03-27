
while True:
    try:
        valor = float(input("Valor em reais: "))
        parcelas = int(input('Número de parcelas: '))
        if parcelas >= 12:
            break
        else:
            print('O valor mínimo de parcelas é 12')
    except:
        print('erro')
if parcelas >= 24 and parcelas < 36:
    valor = (valor * 0.1) + valor
elif parcelas >= 36:
    valor = (valor * 0.15) + valor
    
for n in range(0, parcelas):
    print(f'R$ {(valor/parcelas):.2f}')
