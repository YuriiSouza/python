'''Vamos aprender a criar uma GUI(graphical user interfaces)'''
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

janela = Tk()  

janela.title("Formulário")
janela.geometry('720x720')
n = colorchooser

ttk.Button(janela, text = 'Bem vindo').grid()


janela.mainloop()
