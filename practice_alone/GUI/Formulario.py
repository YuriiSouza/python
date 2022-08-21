'''Vamos aprender a criar uma GUI(graphical user interfaces)'''
from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import tkinter

janela_principal = Tk()  

janela_principal.title("Formulário")
janela_principal.geometry('720x720')

mensagem_inicial = Label(janela_principal, text="formulario")
mensagem_inicial.pack()

'''ttk.Button(janela_principal, text = 'Bem vindo').grid()'''


janela_principal.mainloop()
