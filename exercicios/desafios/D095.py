#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
total = 0
dados = dict()
gols = list()

dados['nome'] = str(input("Qual o nome do jogador? "))
numeroDePartidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))

for n in range(0, numeroDePartidas):
    gols.append(int(input(f"Quantos gols o jogador {dados['nome']} fez no {n + 1}º jogo? ")))
total = sum(gols)

dados['gols'] = gols[:]
dados['total'] = total
