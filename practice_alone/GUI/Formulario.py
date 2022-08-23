'''Vamos aprender a criar uma GUI(graphical user interfaces)'''
''' icons' creator: https://www.flaticon.com/free-icons/flower'''
import tkinter as tk
from tkinter import ttk

def centralizar_window(window, window_widht, window_height):
    centro_x = int(window.winfo_screenwidth() / 2) - int(window_widht / 2)
    centro_y = int(window.winfo_screenheight() / 2) - int(window_height / 2)

    window.geometry(f'{window_widht}x{window_height}+{centro_x}+{centro_y}')


janela_principal = tk.Tk()  
janela_principal.title("Formulário")

centralizar_window(janela_principal, 720, 480)
janela_principal.attributes('-alpha', 1)

janela_principal.iconbitmap('C:/Users/yurip/OneDrive/Documentos/Estudos/hum/python/practice_alone/GUI/Flor.ico')

tk.Label(text = 'Label classico').pack()
ttk.Label(text = 'Label temático').pack()


janela_principal.mainloop()

