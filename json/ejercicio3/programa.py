from funciones import *
doc=leer_json("ej3.json")


# Ejercicio 1
print("Ejercicio 1")

for prov in ListaProvincias(doc):
    print(prov)

# Ejercicio 2
print("Ejercicio 2")

for localidad in ListaLocalidades(doc):
    print(localidad)

# Ejercicio 3
print("Ejercicio 3")
for prov,cant in ListaProvinciasLocalidades(doc):
    print(prov,cant)

# Ejercicio 4
print("Ejercicio 4")
nombre=input("Nombre de provincia:")
localidades = LocalidadesProvincia(doc,nombre)
if len(localidades)>0:
    for localidad in localidades:
        print(localidad)
else:
    print("No existe la provincia")

# Ejercicio 5
print("Ejercicio 5")
nombre=input("Nombre de localidad:")
provincia = ProvinciaLocalidades(doc,nombre)
if provincia!="":
    print(provincia)
else:
    print("No existe localidad.")

# Ejercicio 6
print("Ejercicio 6")

ids = []
id = input("Id. de provincia. 0 para salir")
while id!="0":
    ids.append(id)
    id = input("Id. de provincia. 0 para salir")

for provincia,localidades in ProvinciasLocalidadesID(doc,ids):
    print (provincia)
    for localidad in localidades:
        print(localidad)

