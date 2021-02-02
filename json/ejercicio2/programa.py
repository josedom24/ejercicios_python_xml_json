from funciones import *

doc=leer_json("pruebas.json")
	
# Ejercicio 1
print("Ejercicio 1")
print("Número de pruebas: %d" % len(doc))
print(40*"*")

## Ejercicio 2
print("Ejercicio 2")
for titulo in PruebasMasDeDosHoras(doc):
    print(titulo)
print(40*"*")

## Ejercicio 3
print("Ejercicio 3")
for url in UrlPruebasNoPresencial(doc):
    print(url)
print(40*"*")

## Ejercicio 4
print("Ejercicio 4")
id = input("Dame el id de una prueba:")
datos=PruebaTitulosProfesores(doc,id)
if len(datos)>0:
    print("Título:",datos.get("titulo"))
    print("Profesores")
    for profesor in datos.get("profesores"):
        print(profesor)
else:
    print("No existe esa prueba de nivel")
print(40*"*")

## Ejercicio 5
print("Ejercicio 5")

for titulo,profesores in InfoPrueba(doc):
    print(titulo)
    print("Profesores")
    for profesor in profesores:
        print("\t"+profesor)
print(40*"*")