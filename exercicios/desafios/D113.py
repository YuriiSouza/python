# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(mensagem):
    while True:
        n = input(mensagem)
        if n.isnumeric():
            break
        else:
            print("Valor não é inteiro")
    
    return n