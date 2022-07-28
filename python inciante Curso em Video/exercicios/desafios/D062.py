# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print("=="*8)
print("Criando uma P.A 2.0")
print("=="*8)


primeiroTermo = int(input("Primeiro termo da P.A: "))
razao = int(input("Razão da P.A: "))
cont = 0
termo = primeiroTermo
while cont < 10:
    print(termo)
    termo += razao
    cont += 1
while True:
    verificador = int(input("Visualizar mais quantos termos: "))
    if verificador > 0:
        cont = 0
        while cont < verificador:
            print(termo)
            termo += razao
            cont += 1
    else:
        break
