import tkinter
from tkinter import ttk

window = tkinter.Tk()

label = ttk.Label(text="Juegos:")
label.pack()

lista = ['GTA V','Worms','CSGO', 'AOE3','ACUnity']
lista_items = tkinter.StringVar(value=lista)

list_box = tkinter.Listbox(window, height=10, listvariable=lista_items)
list_box.pack()

window.mainloop()
