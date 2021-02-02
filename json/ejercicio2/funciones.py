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

## Ejercicio 2
def PruebasMasDeDosHoras(doc):
    titulos = []
    for prueba in doc:
        if prueba.get("Horas")>2:
            titulos.append(prueba.get("Titulo"))
    return titulos

## Ejercicio 3
def UrlPruebasNoPresencial(doc):
    urls = []
    for prueba in doc:
        if prueba.get("TipoFormacion")=="NoPresencial":
            urls.append(prueba.get("URL"))
    return urls

## ejercicio 4
# Devuelvo una lista de diccionarios
# Cada diccionario tiene un titulo y una lista de profesores
def PruebaTitulosProfesores(doc,id):
    prueba_encontrada={}
    for prueba in doc:
        if prueba.get("$id")==id:
            prueba_encontrada["titulo"]=prueba.get("Titulo")
            prueba_encontrada["profesores"]=[]
            for profesor in prueba.get("Profesorado"):
                prueba_encontrada.get("profesores").append(profesor.get("NombreCompleto"))
            return prueba_encontrada
    return prueba_encontrada
## ejercicio 5
def InfoPrueba(doc):
    titulos = []
    profesores=[]
    for prueba in doc:
        titulos.append(prueba.get("Titulo"))
        lista_prof = []
        for profesor in prueba.get("Profesorado"):
                lista_prof.append(profesor.get("NombreCompleto"))
        profesores.append(lista_prof)
    return zip(titulos,profesores)


########################
