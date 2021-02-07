from funciones import *
doc=leer_json("metallica.json")

respuesta=menu()
while respuesta!=5:
    if respuesta==1:
        for album,fecha,contenido in listar_discos(doc):
            print(album,"\n",fecha,"\n",contenido,"\n",80*"-")
    elif respuesta==2:
        for album,canciones in contar_canciones(doc):
            print(album,":->",canciones)
    elif respuesta==3:
        inf=int(input("Indica el mínimo número de oyentes:"))
        sup=int(input("Indica el máximo número de oyentes:"))
        for album,etiquetas in filtrar_discos(doc,inf,sup):
            print(album)
            for etiqueta in etiquetas:
                print(etiqueta,", ",end=" ")
            print()
    elif respuesta==4:
        titulo=input("Dime una canción:")
        nombre=buscar_cancion(doc,titulo)
        if nombre!=None:
            print(nombre)
        else:
            print("No encuentro el disco")
    respuesta=menu()
