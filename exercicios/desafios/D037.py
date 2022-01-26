#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 
n = int(input("Digite um número inteiro: "))
p = input("Deseja mudar para qual base: 1.binária\n2.octal\n3.hexadecimal\n").lower()
k = n;
valor = '';
if p == 'binária' or p == 'binaria' or p == 'binario' or p == 'binário' or p == '1':
    
    while True:
        restoDiv = n % 2;
        n = n // 2;
        valor = str(restoDiv) + valor
        if n == 0:
            break
    
    print("Valor {} em binário: {}".format(k, valor))

elif p == 'octadecimal' or p == '2':
    
    while True:
        restoDiv = n % 8;
        n = n // 8;
        valor = str(restoDiv) + valor
        if n == 0:
            break
    
    print("Valor {} em binário: {}".format(k, valor))

elif p == 'hexadecimal' or p == '3':
    
    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']

    while True:
        restoDiv = n % 16;
        n = n // 16;
        valor = hexa[restoDiv] + valor
        if n == 0:
            break
    
    print("Valor {} em binário: {}".format(k, valor))
