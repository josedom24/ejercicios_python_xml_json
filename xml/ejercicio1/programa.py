from funciones import *

# Este objeto es de tipo ElementTree
arbol=leer_xml("provinciasypoblaciones.xml")



#Ejercicio 1
for nombre in lista_provincias(arbol):
	print (nombre)


##Ejercicio 2
for nombre in lista_poblaciones(arbol):
	print (nombre)

## Ejercicio 3
for nombre ,total in lista_provincias_total_poblaciones(arbol):
	print (nombre,total)

## Ejercicio 4
for nombre in poblaciones("Sevilla",arbol):
	print (nombre)

## Ejercicio 5
print(provincia("Utrera",arbol))

## Ejercicio 6
lista_id=[]
id=input("id (con 0 termina):")
while id!="0":
	lista_id.append(id)
	id=input("id (con 0 termina):")

lista=provincias_por_identificador(lista_id,arbol)
for prov in lista:
	nombre=prov[0]
	localidades=prov[1]
	print(nombre)
	for loc in localidades:
		print(loc)


## Ejercicio 7
print(localidades_grandes("Sevilla",arbol))

## Ejercicio 8
print(localidad_grande("Sevilla",arbol))
