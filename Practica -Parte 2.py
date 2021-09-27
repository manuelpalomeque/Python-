#LISTAS     ----------------------------------------------------------------------------
# Dada la siguiente tupla, crear una lista que sólo incluya
# los números menor que 5 utilizando un ciclo for.
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for numero in tupla:
    if numero < 5:
        lista.append(numero)
else:
    print(lista)

# Transformar cada numero multiplicandolo por 2

# Filtrar las comidas que no sean carne
# Encuentra y devuelve la gallina
# Dime donde esta la gallina
# Rellenar la lista de dinero
# esta bien?
# Hay algun error?

#TUPLAS     ----------------------------------------------------------------------------

# Hacer un programa para ingresar cinco números distintos y luego mostrar por
# pantalla el mayor y el menor de ellos.

# Hacer un programa para ingresar cuatro números y luego mostrar por pantalla
# cuáles son mayores a 100.

# Hacer un programa para ingresar cuatro números y luego mostrar por pantalla
# cuántos son menores a 100.

#CICLO WHILE    ---------------------------------------------------------------------------
#aumentar valor de  2 en 2, hasta llegar al  250:
contador = 0

while contador <= 250:
    print('El valor es: ', contador)
    contador += 2
else:
    print('Fin del ciclo ')

#CICLO FOR  -----------------------------------------------------------------------------
# Hacer un programa para mostrar los números del 1 al 10. No se debe realizar
# ningún pedido de datos.
contador1 = 0

for x in range(10):
    contador1 += 1
    print(contador1)

# iterar un rango de 0 a 10 e imprimir numeros divisibles
# entre 3

for i in range(10):
    if i % 3 == 0:
        print(i)
else:
    print('Fin del ciclo')

# Hacer un programa que solicite el ingreso de 10 números y que muestre el
# mayor de ellos por pantalla. Solo se debe emitir UN valor por pantalla.
numeros = []
valor = None
numeroMayor = 0

for x in range(10):
    valor = int(input('Ingrese el valor: '))
    numeros.append(valor)
    if valor > numeroMayor:
        numeroMayor = valor
else:
    print(f'Él numero mas alto es {numeroMayor}, fin del ciclo')

# Hacer un programa que solicite 20 números y calcule y emita por pantalla
# cuántos son positivos (mayores a cero). Se debe mostrar un solo valor: el
# conteo final.
numerosEvaluar = []
contadorPositivos = 0
valor1 = None

for x in range(20):
    valor1 = int(input('Ingrese el valor: '))
    numerosEvaluar.append(valor1)
    if valor1 > 0:
        contadorPositivos += 1
else:
    print(f'La cantidad de numeros positivos son: {contadorPositivos}')

# Hacer un programa para mostrar los números del 10 al 1. No se debe realizar
# ningún pedido de datos.

# Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo:
# 0, 5, 10, 15, 20.... 100.

# Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.
# Nota: un numero es primo cuando es divisible únicamente por 1 y por sí
# mismo.

# Hacer un programa que solicite 10 números y luego mostrar por pantalla el
# máximo de ellos y la posición en la que fue ingresado.

# Hacer un programa que solicite 20 números y luego mostrar por pantalla el
# menor de ellos y la posición en la que fue encontrado.

# Hacer un programa que solicite 20 edades y luego calcule el promedio de edad
# de aquellas personas mayores a 18 años.

# Hacer un programa que solicite 20 números y luego emitir por pantalla el
# máximo de los números pares y el mínimo de los números impares.

# Hacer un programa para ingresar 10 números y luego calcule y emita el mayor
# de los primos de la lista. En caso de no haber ningún número primo, deberá
# aclararlo con un cartel.
