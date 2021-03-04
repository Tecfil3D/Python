# Bucle while
# Ejecuta un bucle mientras la condición sea cierta

# Incrementa 1 a inicio mientras el valor sea menor o igual a final

inicio = 0
final = 10

while inicio < final:
    print(inicio)
    inicio += 1

while inicio < final:
    print(inicio)
    inicio += 1
else:
    print('Inicio ya no es menor que', final)

# Romper la iteración en un determinado punto con break

start = 0
end = 10

while start < end:
    print(start)
    if start == 5:
        break
    start += 1

# Recorrer los elementos de un array

index = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while index < len(lista):
    print(lista[index])
    index += 1
