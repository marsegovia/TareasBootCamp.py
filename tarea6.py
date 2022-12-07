class vehiculo:
    Color = "Blanco"
    Ruedas = 4
    Puertas = 5
    
class Coche(vehiculo):
    Velocidad = 100
    Cilindrada = 4
    
coche = Coche()

print("Color: ",coche.Color)
print("Cant. ruedas: ", coche.Ruedas)
print("Cant. puertas:",coche.Puertas)
print("Velocidad: ",coche.Velocidad, "Km/h")
print("Cilindrado: ",coche.Cilindrada)

