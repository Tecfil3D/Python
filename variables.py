# Variables.

string = 'Hola esto es un string.'
print(string)

string = "Cambiando el valor de string."
print(string)

a, b, c = 1, 4, 7
print('El valor de las variables de a, b y c son:', a, b, c)

# 'del' nos permite eliminar variables.

del a, b, c

string = 'Cadena de texto'
integer = 12
float = 3.14

# Con str convertimos los números int en string para poderlos concatenar,
# concatenamos las comillas vacías para generar un espacio entre los datos.

concatenar = string + ' ' + str(integer) + ' ' + str(float)
print(concatenar)

# Sumar un string + int

string = '4'
integer = 1

# Convertimos el dato string en entero

total = int(string) + integer
print('El total es: ', total)
