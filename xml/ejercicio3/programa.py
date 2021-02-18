from funciones import *

arbol = leer_xml('sevilla.xml')

### Ejercicio 1
lat,lon=latitudylongitud(arbol)
print("Latitud: %s"%lat)
print("Longitud: %s"%lon)

### Ejercicio2
t,v,h=actual(arbol)
print("Temperatura: %s"%t)
print("Viento: %s"%v)
print("Humedad: %s"%h)

### Ejercicio3
pronostico=pronostico(arbol)
for fecha,temp in pronostico.items():
	print(fecha)
	print(temp[0])
	print(temp[1])

### Ejercicio4
t,v,h=buscar("2016-02-27","13:00:00",arbol)
print("Temperatura: %s"%t)
print("Viento: %s"%v)
print("Humedad: %s"%h)
