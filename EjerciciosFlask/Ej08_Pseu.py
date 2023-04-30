#Bisiesto
def principal(anyo):
    try:
        entero = int(anyo)
    except ValueError:
        print("El valor debe ser un año AD (número entero positivo)")
 
    if entero % 4 == 0:
        return(f"El año {anyo} es bisiesto")
    else:
        if entero % 100 == 0 and anyo % 400 == 0:
            return("El año es bisiesto")
        else:
            return(f"El año {anyo} no es bisiesto")
