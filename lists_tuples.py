# Lists ( en las listas los datos se pueden modificar y están contenidos entre corchetes)

lista = ['Manuel', 23, 'hola mundo', 3.14, 'Antonio']
lista[0] = 'Cambiamos de valor'
print(lista[0])
print('Todos los elementos que contiene lista', lista)
print(lista[1:4])    # Extraemos una parte del array lista, desde el index 1 al 4
print(lista[1:])    # Extraemos desde el index 1 al final de la lista
print(lista * 3)    # Extraemos lista 3 veces
nueva_lista = lista * 2    # se puede crear otro array que contenga la lista * 2
print(nueva_lista)

# Concatenar listas

lista1 = ['uno', 'dos', 'tres']
lista2 = ['cuatro', 'cinco', 'seis']
lista_concatenada = lista1 + lista2
print(lista_concatenada)


# Tuples ( en las tuplas los datos no se pueden modificar y están contenidos entre paréntesis)

tuples = ('Manuel', 'Antonio', 35, 3.14)
# tuples [0] = 'cambiamos de valor'    # En tuples no se pueden actualizar/modificar los elementos
print('Todos los elementos que contiene tuples', tuples)
print(tuples[1:4])    # Extraemos una parte del array tuples, desde el index 1 al 4
print(tuples[1:])    # Extraemos desde el index 1 hasta el final del tuples
print(tuples * 3)    # Extraemos tuples tres veces
nuevo_tuples = tuples * 2    # se puede crear otro array que contenga  tuples * 2
print(nuevo_tuples)

#  Concatenar tuples

tuples1 = ['siete', 'ocho', 'nueve']
tuples2 = ['diez', 'once', 'doce']
tuples_concatenado = tuples1 + tuples2
print(tuples_concatenado)
