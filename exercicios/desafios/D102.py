#: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def factorial(number = 0, show = False):
    """
    função para calculo do fatorial do 'number'
    o parametro 'show' recebe 'True' ou 'False'
        True = mostra a multiplicação
        False = apresenta apenas o resultado

    """
    help(factorial)
    fct = 1

    for n in range(1, number + 1):
        fct *= n
        if show == True:
            print(n, end = ' ')
            if n < number:    
                print(end = " x ")
            else:
                print(end = " = ")

    print(fct)


n = int(input("Número: "))
validar = str(input("Gostaria de ver o calculo: ")).lower()[0]
if validar == 's':
    mostrar = True
else:
    mostrar = False

factorial(n, mostrar)
