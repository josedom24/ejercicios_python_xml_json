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

def ListaProvincias(doc):
    prov = []
    for provincia in doc["lista"]["provincia"]:
        prov.append(provincia["nombre"]["__cdata"])
    return prov

def ListaLocalidades(doc):
    loc = []
    for provincia in doc["lista"]["provincia"]:
        if type(provincia["localidades"]["localidad"])==list:
            for localidad in provincia["localidades"]["localidad"]:
                loc.append(localidad["__cdata"])
        else:
            loc.append(provincia["localidades"]["localidad"]["__cdata"])
        
    return loc

def ListaProvinciasLocalidades(doc):
    prov = []
    cantidades = []
    for provincia in doc["lista"]["provincia"]:
        prov.append(provincia["nombre"]["__cdata"])
        if type(provincia["localidades"]["localidad"])==list:
            cantidades.append(len(provincia["localidades"]["localidad"]))
        else:
            cantidades.append(1)
    return zip(prov,cantidades)

def LocalidadesProvincia(doc,nombre):
    loc = []
    for provincia in doc["lista"]["provincia"]:
        if provincia["nombre"]["__cdata"]==nombre:
            if type(provincia["localidades"]["localidad"])==list:
                for localidad in provincia["localidades"]["localidad"]:
                    loc.append(localidad["__cdata"])
            else:
                loc.append(provincia["localidades"]["localidad"]["__cdata"])
    return loc


def ProvinciaLocalidades(doc,nombre):

    for provincia in doc["lista"]["provincia"]:
        if type(provincia["localidades"]["localidad"])==list:
            for localidad in provincia["localidades"]["localidad"]:
                if localidad["__cdata"]==nombre:
                    return provincia["nombre"]["__cdata"]
        else:
            if provincia["localidades"]["localidad"]["__cdata"]==nombre:
                return provincia["nombre"]["__cdata"]
    return ""

def ProvinciasLocalidadesID(doc,ids):
    prov = []
    loc = []
    for provincia in doc["lista"]["provincia"]:
        if provincia["_id"] in ids:
            prov.append(prov.append(provincia["nombre"]["__cdata"]))
            lista_localidad=[]
            if type(provincia["localidades"]["localidad"])==list:
                for localidad in provincia["localidades"]["localidad"]:
                    lista_localidad.append(localidad["__cdata"])
            else:
                lista_localidad.append(provincia["localidades"]["localidad"]["__cdata"])
            loc.append(lista_localidad)
    return zip(prov,loc)


