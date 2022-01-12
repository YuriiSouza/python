n = int(input("Digite um número para ver sua tabuada: "))
cont = 0;
multiplicacao = 1

print( '=' * 20)
while(cont<11):
    multiplicacao = n*cont;
    print("{:2} x {:2} = {}".format(n, cont, multiplicacao))
    cont = cont+1;

print('=' *20)