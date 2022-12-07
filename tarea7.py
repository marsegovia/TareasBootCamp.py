class Alumno:
    def __init__(self,Nombre,Nota):
       self.nombre = Nombre
       self.nota = Nota

alumno = Alumno("Julian",5)
print("\n","Nombre:",alumno.nombre,"\n", "Nota:",alumno.nota)
if alumno.nota > 6:
    print("Aprobado")
else:
   print("No aprobado")   
           

