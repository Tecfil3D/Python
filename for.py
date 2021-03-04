# Bucle for

# range ( inicio, final)

for x in range(0, 10):    # x es una variable que puede ser cualquier otro nombre
    print(x)

# tuples o list

nombres = ('Juan', 'Ramón', 'Rosa', 'Gabriel', 'Ana María')
for index in range(len(nombres)):
    print(nombres[index])
else:
    print('Ya no quedan mas nombres')

# Diccionario

diccionario = {1: 'Juan', 2: 'Ramón', 3: 'Rosa', 4: 'Gabriel', 5: 'Ana María'}
for clave, valor in diccionario.items():
    print(clave, ':', valor)
