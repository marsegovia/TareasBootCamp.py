from pickle import *

class Vehiculo():
    def __init__(self,Color,Puertas):
        self.puertas = Puertas
        self.color = Color
        
    
    
coche =Vehiculo("Rojo",4)
print(coche.color, " ",coche.puertas)  

file = open('vehiculo_objeto', 'w+b')

dump(coche, file)
file.seek(0)
nuevo_coche = load(file)

print(nuevo_coche)
file.close()