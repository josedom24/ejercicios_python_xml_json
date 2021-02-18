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
    

### Ejercicio 1
def lista_provincias(arbol):
	nombres = arbol.xpath('//nombre/text()')	
	return nombres

### Ejercicio 2
def lista_poblaciones(arbol):
	nombres = arbol.xpath('//localidad/text()')
	return nombres

### Ejercicio 3
def lista_provincias_total_poblaciones(arbol):
	lista=[]
	nombres = arbol.xpath('//nombre/text()')
	for provincia in arbol.xpath('//provincia'):
		localidades=provincia.xpath('count(./localidades/localidad)')	
		lista.append(int(localidades))
	return zip(nombres,lista)

### Ejercicio 4
def poblaciones(prov,arbol):
	nombres = arbol.xpath('/lista/provincia[nombre="%s"]//localidad/text()'%prov)
	return nombres



### Ejercicio 5
def provincia(nombre_localidad,arbol):
	localidades=arbol.xpath('//localidades[localidad="%s"]/../nombre/text()'%nombre_localidad)
	return localidades[0]

### Ejercicio 6
def provincias_por_identificador(lista_id,arbol):
	lista=[]
	for id in lista_id:
		provincia=arbol.xpath('//provincia[@id="%s"]/nombre/text()'%id)
		lista_localidades=arbol.xpath('//provincia[@id="%s"]/localidades/localidad/text()'%id)
		lista.append((provincia[0],lista_localidades))
	return lista

### Ejercicio 7
def localidades_grandes(prov,arbol):
	localidades= arbol.xpath('/lista/provincia[nombre="%s"]//localidad[@c="1"]/text()'%prov)
	return(localidades)

### Ejercicio 8
def localidad_grande(nombre_localidad,arbol):
	localidades= arbol.xpath('/lista/provincia/localidades/localidad[text()="%s" and @c="1"]/text()'%nombre_localidad)
	if len(localidades)>0:
		return arbol.xpath('//localidades[localidad="%s"]/../nombre/text()'%nombre_localidad)[0]
	return None




