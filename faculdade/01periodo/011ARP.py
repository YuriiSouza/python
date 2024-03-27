def input_answer():
    answer = ''
    
    while True:
        answer = str(input("Resposta: a/b/c/d"))
        if answer.lower() in 'abcd':
            break
            
    return answer

def selection_tip(number_of_question, tips):
    tip = tips[number_of_question]
    
    return tip
    
def selection_correct_answer(number_of_question, answer_keys):
    answer_key = answer_keys[number_of_question]
    
    return answer_key
    
def wrong_right(answer, correct_answer, tip):
    if answer == correct_answer:
        print("Parabéns, você acertou!")
    else:
        print(f"Ops, parece que sua resposta está incorreta. Aqui está uma dica: {tip}")

tips = ["Use as fórmulas da trigonometria para triângulo retângulo"]#Dicionário com todas as dicas para cada questão
answer_keys = ['a']

numbers_of_questions = 1 #Numéro de questões da lista

for n in range(0, numbers_of_questions):#inicia a correção, para ser configurável com a quantidade de questões
    tip = selection_tip(n, tips)
    correct_answer = selection_correct_answer(n, answer_keys)
    answer = input_answer()
    wrong_right(answer, correct_answer, tip)
    
    