#Cubo
def principal(lado):

    volumen=0
    area=0
    
    #Se comprueba que sea un numero
    try:
            entero=int(lado)
    except ValueError:
            return "El numero debe ser un entero"

    if(int(lado)<0):
        return("Error, el radio no puede ser menor que 0")
    else:
        #Se calcula el area y el volumen
        area=int(lado)*int(lado)*6
        volumen=int(lado)*int(lado)*int(lado)
        return ("Area: {n:1.2f} Volumen: {l:1.2f}".format(n=area,l=volumen))
