año = int(input("ingrese un año: "))

    
def AñoBisiesto(año):
    if año%4==0 and (año%400==0 or not año%100==0):
        print("Es año bisiesto")
    else:
        print("el año no es bisiesto")
        
AñoBisiesto(año)
    