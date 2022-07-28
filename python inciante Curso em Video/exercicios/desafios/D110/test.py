#Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
from utilidades_dev import moeda

p = float(input("Price: "))

moeda.resume_value(p, 10, 20)
