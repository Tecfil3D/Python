# Strings

# Para incluir comillas dentro de las comillas del string, debemos
# hacer uso de la barra inclinada como en el ejemplo.

cadena = "Tutorial \"python\""
print(cadena)

# O bien utilizar las comillas simples para escribir el string y las
# dobles para marcar la palabra

cadena = 'Tutorial "python"'
print(cadena)

# Para imprimir un caracter, indicamos que variable vamos a imprimir
# y entre corchetes indicamos el index donde se encuentra.

saluda = 'Hola mundo '
print(saluda[3])

print(saluda[0:3])    # Para extraer un substring

print(saluda[2:])    # Extraer un substring desde la posición indicada hasta el final

print(saluda * 3)    # Muestra tres veces el string

variable = "Hola "
variable += "Mundo "
variable += "Python "

print(variable)


