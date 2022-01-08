def leituraNotas():
    t = int(input("Nota : "));
    return t    
    
    
def media(x, y):
    media = (x + y)/2;
    return media    
    

n1 = leituraNotas()
n2 = leituraNotas()

mediabimes = media(n1, n2)

if mediabimes > 7.0:
    print("APROVADO");
else:
    print("REPROVADO");