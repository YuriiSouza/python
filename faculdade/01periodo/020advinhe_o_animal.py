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

print("pense em algum desses animais abaixo e responda: ")

for n in animais:
    print(f"..{n}..")

pergunta = str(input("Tem pena? "))
if 'sim' in pergunta:
    animais = ["pato",
    "águia",
    "galinha",
    "avestruz",
    "pinguim"]
    
    pergunta = str(input("Voa? "))
    if 'sim' in pergunta:
        animais = ["pato",
        "águia"]
        
        pergunta = str(input("Nada? "))
        if 'sim' in pergunta:
            animais = ["pato"]
        else:
            animais = ["águia"] 
    else:
        animais = ["galinha",
        "avestruz",
        "pinguim"           
        ]
        
        pergunta = str(input("Nada? "))
        if 'sim' in pergunta:
            animais = ["pinguim"]
        else:
            animais = ["galinha",
            "avestruz"
            ] 
            pergunta = str(input("é grande? "))
            if 'sim' in pergunta:
                animais = ["avestruz"]
            else:
                animais = ["galinha"]          
else:
    animais = ["morcego",
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
    pergunta = str(input("Voa? "))
    if 'sim' in pergunta:
        animais = ["morcego"]
    else:
        animais = ["ornitorrinco",
        "leão",
        "gato",
        "onça pintada",
        "baleia",
        "tubarão",
        "lambari",
        "enguia",
        "arraia"
        ]
        pergunta = str(input("Vive na agua? "))
        if 'sim' in pergunta:
            animais = ["baleia",
                "tubarão",
                "lambari",
                "enguia",
                "arraia"]
            
            pergunta = str(input("é um peixe? "))
            if 'sim' in pergunta:
                animais = ["tubarão",
                    "lambari",
                    "arraia"]
                pergunta = str(input("tem ferrão? "))
                if 'sim' in pergunta:
                    animais = ["arraia"]
                else:
                    pergunta = str(input("São predadores? "))
                    if 'sim' in pergunta:
                        animais = ["tubarão"]
                    else:
                        animais = ["lambari"]
            else:
                animais = ["baleia",
                        "enguia"]
                
                pergunta = str(input("é um mamífero? "))
                if 'sim' in pergunta:
                    animais = ["baleia"]
                else:
                    animais = ["enguia"]
        else:   
            animais = ["ornitorrinco",
            "leão",
            "gato",
            "onça pintada"
            ]
            pergunta = str(input("É um felino? "))
            if 'sim' in pergunta:
                animais = ["leão",
                "gato",
                "onça pintada"]
                pergunta = str(input("tem juba? "))
                if 'sim' in pergunta:
                    animais = ["leão"]
                else:
                    animais = ["gato",
                    "onça pintada"]
                    
                    pergunta = str(input("é pequeno? "))
                    if 'sim' in pergunta:
                        animais = ["gato"]
                    else:
                        animais = ["onça pintada"]
                    
            else:
                animais = ["ornitorrinco"]
                    
                        
                

print(animais[0])
