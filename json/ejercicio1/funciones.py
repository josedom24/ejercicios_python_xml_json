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

def contar_libros(doc):
	return len(doc.get("bookstore").get("book"))

def seleccionar_por_precios(doc,pmax,pmin):
	libros=[]
	for libro in doc.get("bookstore").get("book"):
		precio=float(libro.get("price"))
		if precio<=pmax and precio>=pmin:
			libros.append(libro.get("title").get("__text"))
	return libros

def seleccionar_por_titulo(doc,titulo):
	libros=[]
	for libro in doc.get("bookstore").get("book"):
		if libro.get("title").get("__text").startswith(titulo):
			libros.append((libro.get("title").get("__text"),libro.get("year")))
	return libros	

def seleccionar_autores(doc):
	libros=[]
	for libro in doc.get("bookstore").get("book"):
		autores=[]
		if isinstance(libro.get("author"),list):
			for autor in libro.get("author"):
				autores.append(autor)
		else:
			autores.append(libro.get("author"))
		libros.append((libro.get("title").get("__text"),autores))
	return libros


