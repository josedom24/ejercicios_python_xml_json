
from funciones import *
doc=leer_json("libreria.json")


# Ejercicio 1
print(40*"*")
print("Cuantos libros tenemos:")
print(contar_libros(doc))

# Ejercicio 2
print(40*"*")
precio_min=float(input("Precio mínimo:"))
precio_max=float(input("Precio máximo:"))
print("Libros entre los dos precios:")
for libro in seleccionar_por_precios(doc,precio_max,precio_min):
	print(libro)

#Ejercicio 3
print(40*"*")
cadena=input("Dime el nombre del libro:")
print("Libros que empiezan por esa cadena:")
for titulo,año in seleccionar_por_titulo(doc,cadena):
	print(año,titulo)

# Ejercicio 4
print(40*"*")
print("Libros y autores:")
for titulo,autores in seleccionar_autores(doc):
	print(titulo)
	for autor in autores:
		print(autor)	
	print("")

