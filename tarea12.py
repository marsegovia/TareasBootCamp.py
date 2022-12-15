lista = []

pais = input("Ingrese un pais:")

while pais not in lista:
    lista.append(pais)
    pais = input("Ingrese otro pais:")
    
print(sorted(lista))
