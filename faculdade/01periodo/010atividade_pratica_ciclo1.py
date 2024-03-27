def print_welcome_message(message):
    message_length = len(message)
    border_length = 40

    dots_each_side = (border_length - message_length) // 2
    print("." * dots_each_side + message + "." * dots_each_side)
    
def input_idade():
    idade = ''
    do = True
    while do:
        do = False
        try:
            idade = int(input("Idade:"))
        
        except:
            do = True
            
    return idade
    
def eleitor(idade):
    if idade >= 16:
        print("Você é elegível para votar na eleição estudantil!")
    else:
        print("Desculpe, você ainda não tem idade suficiente para votar na eleição estudantil.")
    
    
print_welcome_message('Boas Vindas')

idade = input_idade()

eleitor(idade)
