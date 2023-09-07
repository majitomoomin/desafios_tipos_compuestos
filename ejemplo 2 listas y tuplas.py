#definir una tupla con tres valores enteros. convertir el contenido de
#la tupla a tipo lista. Modificarla la lista y luego convertirla en tupla
fechatupla1=(25, 12, 2016)
print(fechatupla1)
#copiamos la tupla en una lista
fechalista=list(fechatupla1)
print("imprimamos la lista que se le copio la tupla anterior")
print(fechalista)
#modificamos la lista
fechalista [0]=31
print("Imprimamos la lista ya modificada")
print(fechalista)
#copiamos la lista modificada a una tupla
fechatupla2=tuple(fechalista)
print("imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)
