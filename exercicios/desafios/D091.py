#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep

dados = dict()
dadosRanking = list()

for n in range(0, 4):
    dados[f'Player {n + 1}'] = randint(0, 9)
for x, y in dados.items():
    print(f"{x} = {y}")

dadosRanking = sorted(dados.items(), key = itemgetter(1), reverse = True)
print("-==RANKING OF PLAYER==-")

for x, y in enumerate(dadosRanking):
    print(f"{x + 1}º place goes to {y[0]}  with {y[1]} points")
    sleep(1)
