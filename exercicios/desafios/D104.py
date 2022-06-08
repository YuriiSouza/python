#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')
def leiaint(mensagem):
    while True:
        n = input(mensagem)
        if n.isnumeric():
            break
        else:
            print("Valor não é inteiro")
    
    return n

j = leiaint("Numero: ")

print(j)