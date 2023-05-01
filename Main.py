import os
import platform
from prettytable import PrettyTable
from termcolor import colored
import EjercicioBBDD
from EjerciciosFlask import mainApp

def principal():
        
    while True:


        tabla = PrettyTable()
        tabla.field_names = ["Bienvenidos"]
        tabla.align["Bienvenidos"] = "c"
        tabla.add_row([colored("Menu principal", "red")])
        print(colored(tabla.get_string(), "red"))

        tabla = PrettyTable()
        tabla.field_names = ["#", "Descripción"]
        tabla.align["Descripción"] = "l"
        tabla.add_row([colored("1", "blue"), colored("Ejercicio de BBDD", "green")])
        tabla.add_row([colored("2", "blue"), colored("Ejercicio Flask", "green")])
        tabla.add_row([colored("0", "blue"), colored("Salir", "green")])
        print(colored(tabla.get_string(), "blue"))
        opcion = input("Seleccione una opción:")
        if opcion == "1":
            EjercicioBBDD.principal()
        elif opcion == "2":
            mainApp.principal()
        elif opcion == "0":
            print("Adios :)")
            break
        continuar=input("Presione enter para continuar...")

if __name__ == "__main__":
    principal()