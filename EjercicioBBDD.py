from pymongo.mongo_client import MongoClient
import os
import random
import json

#Connect to the database
def connectdb():
    clientDB = MongoClient('mongodb://localhost:27017/')
    return clientDB

#Create a database
def CreateDB(name,clientDb):
    database_name=name 
    db=clientDb[database_name]
    return db

#Create a collection
def createCollection(name,db):
    collection_name=name 
    collection=db[collection_name]
    return collection

def generar_lista_aleatoria():
        lis = [random.choice(["H", "M"]) for _ in range(100)]
        lista = list()
        for i in range(100):
             lista.append({"Persona":lis[i]})
        return lista, lis
    
def clasificar_genero(lista):
        hombres = lista.count("H")
        mujeres = lista.count("M")
        porcentaje_hombres = (hombres / len(lista))*100
        porcentaje_mujeres = (mujeres / len(lista))*100
        return hombres, mujeres, porcentaje_hombres, porcentaje_mujeres
    
def guardar_lista_en_bbdd(lista, col):
        documents=lista
        col.insert_many(documents)

def cargar_lista_desde_bbdd(col):
        try:
            result=col.find({}).limit(200)
            for i in result:
                print(i)
        except:
            return None

if __name__=="__main__":
    client=None
    db=None
    col=None
    client = connectdb()
    db=CreateDB('EOI',client)
    col=createCollection('Generos',db)
    opcion = input("""
       Elige una opción:\n
       1. Generar lista aleatoria\n
       2. Recuperar lista de la BBDD o generar nueva\n
       """)
    if opcion == "1":
        lista, lis = generar_lista_aleatoria()
        guardar_lista_en_bbdd(lista, col)
    elif opcion == "2":
        lista = cargar_lista_desde_bbdd(col)
        if lista is None:
            lista, lis = generar_lista_aleatoria()
            guardar_lista_en_bbdd(lista, col)
    else:
        print("Opción no válida")
        exit()
    hombres, mujeres, porcentaje_hombres, porcentaje_mujeres = clasificar_genero(lis)

    print(f"Numero de hombres: {hombres}")
    print(f"Numero de mujeres: {mujeres}")
    print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
    print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")

    opcion_guardar = input("¿Deseas guardar los resultados en un archivo? (s/n)\n")
    if opcion_guardar.lower() == "s":
        resultados = {
            "num_hombres": hombres,
            "num_mujeres": mujeres,
            "porcentaje_hombres": round(porcentaje_hombres,2),
            "porcentaje_mujeres": round(porcentaje_mujeres,2)
        }
        col=createCollection('ResultadosGeneros',db)
        col.insert_one(resultados)
        