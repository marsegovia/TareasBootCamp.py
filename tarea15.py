import tkinter
from tkinter import ttk

window = tkinter.Tk()

label = tkinter.Label(window, text="Juegos:")
label.grid(column=0, row=0)

lista = ['GTA V','Worms','CSGO', 'AOE3','ACUnity']
lista_items = tkinter.StringVar(value=lista)

list_box = tkinter.Listbox(window, height=10, listvariable=lista_items, )
list_box.grid(column = 0, row=0, sticky= tkinter.W)


window.mainloop()