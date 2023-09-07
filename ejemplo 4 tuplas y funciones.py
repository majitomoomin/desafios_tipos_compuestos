#desarrollar una funcion que solicite la carga del día, mes y año y
#almacene dicgos datos en una tupla que luego debe retonar.
#la segunda funcion a implementar debe recibir una tupla
#con la fecha y mostrarla por pantalla
def cargar_fecha():
    dd=int(input("Ingrese numero de día: "))
    mm=int(input("ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año: "))
    return (dd, mm, aa)


def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")


#bloque principal
fecha=cargar_fecha()
imprimir_fecha(fecha)
