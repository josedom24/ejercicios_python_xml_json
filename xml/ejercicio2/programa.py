from funciones import *

# Este objeto es de tipo ElementTree
arbol=leer_xml("users.xml")

### Ejercicio 1
print(usuarios(arbol))

### Ejercicio 2
print(avatar(arbol))

### Ejercicio 3
print(acceso_desde_fuera(arbol))

### Ejercicio 4
cad=input("Dame el nombre:")
print(buscar(cad,arbol))

### Ejercicio 5
dic=lista_por_localidad(arbol)
for key,value in dic.items():
	print(key)
	print("="*len(key))
	for user in value:
		print(user)

### Ejercicio 6
print(ultimo_acceso(arbol))