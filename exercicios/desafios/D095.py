#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
total = 0
dados = dict()
gols = list()
time = list()

while True:
    while True:
        dados['nome'] = str(input("Qual o nome do jogador? "))
        if int(dados["nome"]) == False:
            print("ERRO")
        else:
            break

    while True:
        try:    
            numeroDePartidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
            break
        except:
            print("ERRO")


    for n in range(0, numeroDePartidas):
        while True:
            gols.append(int(input(f"Quantos gols o jogador {dados['nome']} fez no {n + 1}º jogo? ")))
            if type(gols[len(gols) - 1]) == int:
                break
    total = sum(gols)

    dados['gols'] = gols[:]
    gols.clear()
    dados['total'] = total
    time.append(dados.copy())
    dados.clear()
    
    while True:
        n = str(input("Deseja inserir mais jogadores: ")).lower()
        if n in 'sn':
            break
        else:
            print("ERRO")

    if n == 'n':
        break

print("-="*15)
print(f'{"Cod":<5}{"Nome":<10}{"Goals":<10}{"Total":<10}')
for k, v in enumerate(time):
    print(f'{k:<5}', end = "")
    for x in v.values():
        print(f'{str(x):<10}', end = "")
    print("")
