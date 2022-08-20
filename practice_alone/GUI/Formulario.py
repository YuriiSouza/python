'''Vamos aprender a criar uma GUI(graphical user interfaces)'''
from tkinter import *
from tkinter import ttk

janela = Tk()  

janela.title("Formulário")
janela.geometry('720x720')
janela.configure(background= 'black')

ttk.Button(janela, text = 'Bem vindo').grid()


janela.mainloop()
