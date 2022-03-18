#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.
times = ("Atlético", "Flamengo", "Palmeiras","Fortaleza","Corinthians","Bragantino","Fluminense","América","Atlético","Santos","Ceará","Internacional","São Paulo","Athletico","Cuiabá","Juventude","Grêmio","Bahia","Sport","Chapecoense")

print("=-"*15)
print("PRIMEIROS COLOCADOS")
print("=-"*15)
for n in range(0,5):
    print(f"{n+1}º Lugar = {times[n]}")

print("=-"*15)
print("ULTIMOS COLOCADOS")
print("=-"*15)
for n, t in enumarete(times):
     print((f"{len(times)-n}º lugar = {times[len(times)-n]}"))