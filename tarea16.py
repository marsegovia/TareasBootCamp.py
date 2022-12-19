import sqlite3

    
conn = sqlite3.connect("Alumnos.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE Alumnos(id, nombre TEXT, apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES('1','Lionel', 'Scaloni')")
cursor.execute("INSERT INTO Alumnos VALUES('2','Lionel', 'Messi')")
cursor.execute("INSERT INTO Alumnos VALUES('3','Julian', 'Alvarez')")
cursor.execute("INSERT INTO Alumnos VALUES('4','Angel', 'Di Maria')")
cursor.execute("INSERT INTO Alumnos VALUES('5','Enzo', 'Fernandez')")
cursor.execute("INSERT INTO Alumnos VALUES('6','Emiliano', 'Martinez')")
cursor.execute("INSERT INTO Alumnos VALUES('7','Alexis', 'Mac Allister')")
cursor.execute("INSERT INTO Alumnos VALUES('8','Rodrigo', 'De Paul')")

conn.commit()

cursor.execute("SELECT * FROM Alumnos WHERE nombre= 'Lionel'")

alumnos = cursor.fetchall()
print(alumnos)

conn.close()
