#Dado un numero entero, determinar si es par o impar
def principal(parimpar):
    #Se comprueba que sea un numero    
    
    try:
            entero=int(parimpar)
    except ValueError:
            return("El numero debe ser un entero")


    if(int(parimpar)%2!=0):
        return "El numero es impar"
    else:
        return "El numero es par"
if __name__ == '__main__':
   principal()