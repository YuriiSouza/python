#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco','seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    numeroEscolhidoUsuario = int(input("Escreva um número de 0 a 20: "))
    if numeroEscolhidoUsuario >= 0 or numeroEscolhidoUsuario <= 20:
        break;

#print(extenso[numeroEscolhidoUsuario])

for c, p in enumerate(extenso):
    if  c == numeroEscolhidoUsuario:
        print(p)
        