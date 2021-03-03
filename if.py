# Sentencia if

#  if (condición) :
#      Si la condición es cierta
#  else:
#      Si la condición no es cierta

# Operadores de comparación
# igualdad = =
# distinto ! =
# mayor que >
# mayor o igual que > =
# menor que <
# menor o igual que < =

variable = 6

if variable > 5:
    print(variable, 'si es mayor a 5')
elif variable == 5:
    print(variable, 'es igual a 5')
else:
    print(variable, 'no es mayor a 5')

# Operadores lógicos

# and :  las dos condiciones son ciertas
# or : al menos una de las condiciones ha de ser cierta
# not : la condición no es cierta

variable1 = 2
variable2 = 2
variable3 = 3
variable4 = 4

# Si se cumple...

if variable1 == variable2 and variable3 < variable4:
    print('La condición se cumple')
else:
    print('La condición no se cumple')

# Si no se cumple...

if not variable1 == variable2 and variable3 < variable4:
    print('La condición no se cumple')
else:
    print('La condición si se cumple')


# Operador membership nos va a permitir comprobar valores en strings, list y tuples
# in : el valor es encontrado
# not in : el valor no es encontrado

lista = ['uno', 'dos', 'tres']

# Si 'dos' esta en el lista ejecuta

if 'dos' in lista:
    print('se encuentran en la lista')
else:
    print('no se encuentra en la lista')

# Si 'dos' no esta en la lista ejecuta

if 'dos' not in lista:
    print('No se encuentran en la lista')
else:
    print('Si se encuentra en la lista')
