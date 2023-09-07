#En el bloque principal definir un diccionario que almacene
#los nombres de aises como clave y como valor la cantidad de habitantes
#implementar una funcion para mostrar cada clave y valor
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

#bloque principal
paises={"argentina":4000000, "españa":46000000, "brasil": 1900000000, "uruguay": 340000000}
imprimir(paises)
