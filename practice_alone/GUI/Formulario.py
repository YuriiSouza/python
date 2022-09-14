'''Vamos aprender a criar uma GUI(graphical user interfaces)'''
''' icons' creator: https://www.flaticon.com/free-icons/flower'''
import tkinter as tk
from tkinter import ttk
from turtle import back

def centralizar_window(window, window_widht, window_height):
    centro_x = int(window.winfo_screenwidth() / 2) - int(window_widht / 2)
    centro_y = int(window.winfo_screenheight() / 2) - int(window_height / 2)

    window.geometry(f'{window_widht}x{window_height}+{centro_x}+{centro_y}')


def button_clicked():
    print('"Click"')


def select(opção):
    print(opção)


def retornar(event):
    print("OI")


def click():
    print('Voce clicou...')

def log(event):
    print(event)



colorbgLabel = '#4F4F4F'
#configuração da borda da janela
janela_principal = tk.Tk()  
janela_principal.title("Formulário")
janela_principal.iconbitmap('C:/Users/yurip/OneDrive/Documentos/GitHub/python/practice_alone/GUI/Flor.ico')


#configuração de dimensão e layout da janela
centralizar_window(janela_principal, 720, 480)
janela_principal.attributes('-alpha', 1)


#Layout dentro da janela
tk.Label(text = 'Label classico').pack()
ttk.Label(text = 'Label temático').pack()

ttk.Button(janela_principal, text = 'cutuque', command=button_clicked).pack()
ttk.Button(janela_principal, text = 'Sonhar', command=lambda : select('Sonhar')).pack()
ttk.Button(janela_principal, text = 'Realizar', command=lambda : select('Realizar')).pack()

#Event biding-associar um evento a uma função
evento_teste = ttk.Button(
    janela_principal, 
    text= 'evento', 
    command=click)
    #criei o botão, e coloquei um evento para acontecer caso alguem clique nele

evento_teste.bind('<Return>', retornar)#relacionei o evento ao botão, o evento return se refere ao click do enter
evento_teste.bind('<Return>', 
    log, 
    add = '+')

evento_teste.pack()

#evento_teste.unbind('<Return>')Retirando a ligação do evento_teste

#Laber e suas opções
labelTop = ttk.Label(
    janela_principal ,
    text = '012345', 
    anchor = tk.W, 
    background = colorbgLabel, 
    borderwidth = True, 
    font = ("arial", 23), 
    underline = 0)

labelTop.pack(ipadx=100, ipady=100)

janela_principal.mainloop()
