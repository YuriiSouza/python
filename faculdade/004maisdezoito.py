print("Começou")

while True:
    idade = input("Coloque sua idade: ")
    
    if idade in "0123456789" and idade:
        idade = int(idade)
        break
    else:
        idade = None

if idade >= 18:
    print("ok, pode passar")
else:
    print("sai")
    