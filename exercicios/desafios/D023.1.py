numero = str(input("Digite um número de 0 a 9999: "))
n = len(numero)


if(n == 1):
    print("Unidade: {}".format(numero[0]))
elif(n == 2):
    print("Unidade: {}".format(numero[0]))
    print("Dezena: {}".format(numero[1]))
elif(n == 3):
    print("Unidade: {}".format(numero[0]))
    print("Dezena: {}".format(numero[1]))
    print("Centena: {}".format(numero[2]))
elif(n == 4):
    print("Unidade: {}".format(numero[0]))
    print("Dezena: {}".format(numero[1]))
    print("Centena: {}".format(numero[2]))
    print("Milhar: {}".format(numero[3]))
