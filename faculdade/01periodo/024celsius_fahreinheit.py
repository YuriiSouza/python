
def print_temp(celsius, fahrenheit):
    print(f"{celsius:.2f} ºC")        
    print(f"{fahrenheit} ºF")   
    

while True:
    temperatura = str(input("Temperatura: ºC ou ºF: "))
    temperatura = temperatura.split('°')
    
    valor = float(temperatura[0].lower())
    
    try:
        tipo = temperatura[1].lower()
    except:
        tipo = ''
    
    if "c" in tipo:
        temperatura_celsius = valor
        temperatura_fa = (1.8 * valor) + 32
        print_temp(temperatura_celsius, temperatura_fa)
        break
    
    elif "f" in tipo:
        temperatura_celsius = (valor - 32) / 1.8
        temperatura_fa = valor
        print_temp(temperatura_celsius, temperatura_fa)
        break
    
    else:
        print(f"Unidade de medida não reconhecida, formato({valor}°C)")
     