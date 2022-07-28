# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leia_int(mensagem):
    while True:
        try:   
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print("Valor inválido...")
        except (KeyboardInterrupt):
            print("Quis parar...")
            break
        else:
            return n


def leia_float(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except(ValueError, TypeError):
            print("Valor inválido...")
        except (KeyboardInterrupt):
            print("Saiu")
            break
        else:
            return n

print(leia_int('valor inteiro: '))
print(leia_float('Valor real apenas: '))
