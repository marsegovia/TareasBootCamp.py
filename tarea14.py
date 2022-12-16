import tkinter
from tkinter import ttk


window = tkinter.Tk()
def seleccionar1(event):
    print("Ha seleccionado el boton 1")
    
def seleccionar2(event):
    print("Ha seleccionado el boton 2")
    
def seleccionar3(event):
    print("Ha seleccionado el boton 3")
    
def reset(event):
    print("Reiniciado!, Seleccione una opcion:")
    selected.set(None)
    
label = tkinter.Label(window, text="Seleccione una opcion:")
label.grid(column=0, row=0)

selected = tkinter.StringVar()
selected.set(None)

boton1 = ttk.Radiobutton(window, text="B1", value= '1' ,variable= selected)
boton2 = ttk.Radiobutton(window, text="B2", value= '2' ,variable= selected)
boton3 = ttk.Radiobutton(window, text="B3", value= '3' ,variable= selected)
boton = tkinter.Button(window, text="reset")
boton1.grid()
boton2.grid()
boton3.grid()
boton.grid(column=0, row=4)
boton1.bind('<Button-1>', seleccionar1)
boton2.bind('<Button-1>', seleccionar2)
boton3.bind('<Button-1>', seleccionar3)
boton.bind('<Button-1>', reset)


window.mainloop()
