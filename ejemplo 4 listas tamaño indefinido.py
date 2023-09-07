#tamaño indefinido
#realizar la carga de valores enteros por teclado.
#almacenarlos en una lista. finalizar la carga de enteros al ingresar el cero
#mostrar finalmente el tamaño de la lista.
lista=[]
valor=int(input("ingresar valor (0 para fianalizar): "))
while valor!=0:
    lista.append(valor)
    valor=int(input("ingresar valor(0 para finalizar): "))

print("Tamaño de la lista: ")
print(len(lista))
