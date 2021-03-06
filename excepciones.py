# Excepciones try-except

entero = input('Introduzca un numero entero: ')    # Guardamos en la variable entero el valor ingresado

try:
    entero = int(entero)    # condición que debe tener entero para que sea valido el mensaje
    print('El numero es valido, el numero ingresado es:', entero)
except ValueError:    # si no es así, muestra este valor de error
    print('El numero ingresado no es un numero entero')
