#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

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

print("")
print(dados)

print("")
for x, y in dados.items():
    print(f"{x} tem valor de {y}")

print("")
print("+-"*10)
print(f"O jogador {dados['nome']} jogou {numeroDePartidas} partidas:")
for x, y in enumerate(gols):
    print(f"Na partida {x + 1} ele fez {y}")
print("Fez ai todo: ", total)
