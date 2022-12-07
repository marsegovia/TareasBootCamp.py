class vehiculo:
    def __init__(self, Color, Puertas, Ruedas):
       self.Color = Color 
       self.Puertas = Puertas
       self.Ruedas = Ruedas
       
class Coche(vehiculo):
    def __init__(self, Color, Puertas, Ruedas, Velocidad, Cilindrada): 
        self.Color = Color 
        self.Puertas = Puertas
        self.Ruedas = Ruedas
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
       
coche = Coche("Blanco", 5, 4, 100, 1200)
print("\n","Color:",coche.Color,"\n", "Puertas:",coche.Puertas,"\n", "Ruedas:",coche.Ruedas,"\n", 
      "Velocidad:",coche.Velocidad,"\n", "Cilindrada:",coche.Cilindrada)



