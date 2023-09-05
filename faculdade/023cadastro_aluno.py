cadastros_alunos = {
}

todas_matriculas = cadastros_alunos.keys()

print("Informe sua matrícula: ")
matricula = int(input("Matrícula: "))

try:
    print(cadastros_alunos[matricula])
except:
    while True:
        try:
            nome = str(input("Nome: "))
            break
        except:
            print("Erro")
            
    while True:
        try:
            genero = str(input("Gênero: "))
            if genero.lower() in "mf":
                break
        except:
            print("Erro")
                
    while True:
        try:
            curso = str(input("Curso: "))
            if curso.lower() == "bes" or curso == "bec" or curso =="ads":
                break
        except:
            print("Erro")
                
    while True:
        try:    
            coeficiente_de_rendimento = int(input("Coeficiente de rendimento: "))
            if coeficiente_de_rendimento >= 0 and coeficiente_de_rendimento <= 100:
                break
        except:
            print("Erro")
            
    cadastros_alunos[matricula] = {"Nome": nome,
                  "Gênero": genero,
                  "Curso": curso,
                  "Coeficiente de rendimento": coeficiente_de_rendimento,
                  }
    
dados = cadastros_alunos[matricula]

print(f'Nome: {dados["Nome"]}')

if dados["Gênero"] == 'm':
    print('Gênero: Masculino')
else:
    print('Gênero: Feminino')

if dados["Curso"] == 'bes':
    print('Curso: Bacharelado em Engenharia de Software')
elif dados["Curso"] == 'bec':
    print('Curso: “Bacharelado em Engenharia de Computação')
else:
    print('Curso: Analise e Desenvolvimento de Sistemas')
    
if dados["Coeficiente de rendimento"] > 90:
    print('Coeficiente de rendimento: Escelente')
elif dados["Coeficiente de rendimento"] > 70 and dados["Coeficiente de rendimento"] <= 90:
    print('Coeficiente de rendimento: Bom')
elif dados["Coeficiente de rendimento"] > 50 and dados["Coeficiente de rendimento"] <= 70:
    print('Coeficiente de rendimento: Regular')
elif dados["Coeficiente de rendimento"] > 30 and dados["Coeficiente de rendimento"] <= 50:
    print('Coeficiente de rendimento: Necessita melhorar')
elif dados["Coeficiente de rendimento"] >= 0 and dados["Coeficiente de rendimento"] <= 30:
    print('Coeficiente de rendimento: Preucupante')
    