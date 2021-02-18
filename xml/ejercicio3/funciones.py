from lxml import etree
import sys
def leer_xml(fichero):
    try:
        with open(fichero) as f:
            datos=etree.parse(fichero)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

# Ejercicio 1

def latitudylongitud(arbol):
	latitud=arbol.xpath("//latitud/text()")[0]
	longitud=arbol.xpath("//longitud/text()")[0]
	return latitud,longitud

# Ejercicio 2

def actual(arbol):
	temp=arbol.xpath("//condiciones_actuales/temperatura/text()")[0]
	viento=arbol.xpath("//condiciones_actuales/viento/text()")[0]+" "+arbol.xpath("//condiciones_actuales/viento/@direccion")[0]
	humedad=arbol.xpath("//condiciones_actuales/humedad/text()")[0]
	return temp,viento,humedad

# Ejercicio 3
# Voy a crear un diccionario: key la fecha, y valor: temperatura máxima y mínima en una tubla
def pronostico(arbol):
	pro={}
	pronostico=arbol.xpath("//pronostico_dias/dia/@fecha")
	for dia in pronostico:
		pro[dia]=(arbol.xpath('//pronostico_dias/dia[@fecha="%s"]/maxima/text()'%dia)[0],arbol.xpath('//pronostico_dias/dia[@fecha="%s"]/minima/text()'%dia)[0])

	return pro

# Ejercicio 4
def buscar(fecha,hora,arbol):
	horas=arbol.xpath("//pronostico_horas/hora/@id")
	fechas=arbol.xpath("//pronostico_horas/hora/@fecha")
	for hora,fecha in zip(horas,fechas):
		temp=arbol.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/temperatura/text()'%(hora,fecha))[0]
		viento=arbol.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/viento/text()'%(hora,fecha))[0]+" "+arbol.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/viento/@direccion'%(hora,fecha))[0]
		humedad=arbol.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/humedad/text()'%(hora,fecha))[0]
		return temp,viento,humedad
	return None

