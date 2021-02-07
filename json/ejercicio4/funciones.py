import json
import sys

def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

def menu():
    menu='''1.- Listar discos
2.- Contar canciones
3.- Filtrar discos
4.- Buscar por canción
5.- Salir'''
    print(menu)
    opcion=int(input("Opción:"))
    while opcion<1 or opcion>5:
        print("Error")
        opcion=int(input("Opción:"))
    return opcion

# Ejercicio 1
def listar_discos(discos):
    lista=[]
    for disco in discos:
        datos=[]
        datos.append(disco.get("album").get("name"))
        datos.append(disco.get("album").get("wiki").get("published").split(",")[0])
        datos.append(disco.get("album").get("wiki").get("content"))
        lista.append(datos)
    return lista

# Ejercicio 2
def contar_canciones(discos):
    lista=[]
    for disco in discos:
        datos=[]
        datos.append(disco.get("album").get("name"))
        datos.append(len(disco.get("album").get("tracks").get("track")))
        lista.append(datos)
    return lista

# Ejercicio 3
def filtrar_discos(discos,linf,lsup):
    lista=[]
    for disco in discos:
        oyentes=int(disco.get("album").get("listeners"))
        if oyentes>=linf and oyentes<lsup:
            etiquetas=[]
            for etiqueta in disco.get("album").get("tags").get("tag"):
                etiquetas.append(etiqueta.get("name"))
            # En la la lista guardo una tupla, con una cadena de caracteres (el nombre) y una lista de eqtiquetas
            lista.append((disco.get("album").get("name"),etiquetas))
    return(lista)

# Ejercicio 4:
def buscar_cancion(discos,titulo):
    for disco in discos:
        for cancion in disco.get("album").get("tracks").get("track"):
            if cancion.get("name")==titulo:
                return disco.get("album").get("name")
    return None

