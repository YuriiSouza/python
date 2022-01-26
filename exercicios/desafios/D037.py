#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 
n = int(input("Digite um número inteiro: "))#O usuatio digita um numero

p = input("Deseja mudar para qual base:\n 1.binária\n2.octal\n3.hexadecimal\n").lower()#o usuario digita pra qual base ele quer, o .lower()serve para deixar oq o usuario digitar em minusculo
k = n;#O computador coloca o que ta dentro de 'n' na variavel 'k'
valor = '';#Criei uma variavel valor

if p == 'binária' or p == 'binaria' or p == 'binario' or p == 'binário' or p == '1':#o computador ve SE (if) o p (que é a variavel que o compuador colocou o tipo de base que ele converter) é igual a binario binaria e etc, q são os valores que podem aparecer quando o usuario digitar
    
    while True:#figura de repetição que determina o seguinte: enquanto(while) for verdadeiro ele vai funcionar, true sempre vai ser verdadeiro então ele roda infinito, so vai parar quando o if n == 0 for verdadeiro e fazer o comando break funcionar
        restoDiv = n % 2;#aqui é sobre conversão de bases, que vc divide pela base(no caso 2 aqui) e pega os restos ate o valor da divisão interia ser 0
        n = n // 2;
        valor = str(restoDiv) + valor#o unico ponto é que o valores do resto da divisão tem que ser colocados de tras pra frente, então tem que ficar atento com a ordem dessa linha
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
    
    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    while True:
        restoDiv = n % 16;
        n = n // 16;
        valor = hexa[restoDiv] + valor
        if n == 0:
            break
    
    print("Valor {} em binário: {}".format(k, valor))
else:
    print("Valor inválido...")
