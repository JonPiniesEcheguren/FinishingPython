#Cambiar de grados celsius a farenheit

def principal(grados):

    
    try:
            entero=int(grados)
    except ValueError:
            print("El numero debe ser un entero")
    #Se hacen las operaciones
    resultado= float(grados) * (9/5) +32
    return resultado
if __name__ == "__main__":
       principal()
        
