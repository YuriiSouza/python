notaA = float(input("Nota 1: \n"))
notaB = float(input("Nota 2: \n"))

#CalculoDaMédia:
media = (notaA + notaB)/2

#EstruturaCondicional
if (media > 7.0):
    print("Média: %.2f\nRESULTADO...\nAprovado."% media);
else:
    print("Média: %.2f\nRESULTADO...\nReprovado."% media);
