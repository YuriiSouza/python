#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
while True:
    n = int(input("Base: "))
    if n < 0:
        print("PROCESSO ENCERRADO")
        break
    for i in range(1,11):
        print(f"{i:2}  X {n:2} = {n*i:2}")
    