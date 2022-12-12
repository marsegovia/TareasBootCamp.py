txt = open("archivo.txt","w")
texto = txt.write("Creando primer archivo\n")
txt.close()

txt = open("archivo.txt","r+")
txt.readline()
texto = txt.write("Creando primer archivo\n")

txt.close()
