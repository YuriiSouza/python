animais = ["pato",
    "águia",
    "galinha",
    "avestruz",
    "pinguim",
    "morcego",
    "ornitorrinco",
    "leão",
    "gato",
    "onça pintada",
    "baleia",
    "tubarão",
    "lambari",
    "enguia",
    "arraia"
    ]

pergunta = str(input("Tem pena?"))

if 'sim' in pergunta:
    excluir = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]
    for n in excluir:
        animais.pop(n)
else:
    pergunta = False

print(animais)
