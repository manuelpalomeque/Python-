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
    print(f'El valor es: {contador}')
    contador += 2
else:
    print('Fin del ciclo ')

# Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo:
# 0, 5, 10, 15, 20.... 100.
cont = 0

while cont <= 100:
    print(cont)
    cont += 5
else:
    print('Fin del ciclo')

#CICLO FOR  -----------------------------------------------------------------------------
# Hacer un programa para mostrar los números del 1 al 10. No se debe realizar
# ningún pedido de datos.
contador1 = 0

for x in range(10):
    contador1 += 1
    print(contador1)

# Hacer un programa para mostrar los números del 10 al 1. No se debe realizar
# ningún pedido de datos.
contador2 = 11

for x in range(10):
    contador2 -= 1
    print(contador2)

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

print(f'La cantidad de numeros positivos son: {contadorPositivos}')

# Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.

cont = 0
valor= int(input('Ingrese los valores: '))

for x in range(1, valor):
    if  valor % x == 0:
        cont += 1

if cont == 2:
    print('El numero es primo')
else:
    print('No es primo')

# Hacer un programa que solicite 10 números y luego mostrar por pantalla el
# máximo de ellos y la posición en la que fue ingresado.
numMayor = 0
contPosicion = 0

for x in range(10):
    valores = int(input('Por favor ingrese el valor: '))
    if valores > numMayor:
        numMayor = valores
        contPosicion = x +1

print(f' El numero mayor es {numMayor} y se ingreso en la  posicion {contPosicion}')

# Hacer un programa que solicite 20 números y luego mostrar por pantalla el
# menor de ellos y la posición en la que fue encontrado.
numMen = None
posicionMinimo = None

for x in range(20):
    valoresMinimos = int(input('Por favor ingrese el valor: '))
    if x == 0:
        numMen = valoresMinimos
    elif valoresMinimos < numMen:
        numMen = valoresMinimos
        posicionMinimo = x +1

 print(f'El numero menor es {numMen} y se ingreso en la posicion {posicionMinimo}')

# Hacer un programa que solicite 20 edades y luego calcule el promedio de edad
# de aquellas personas mayores a 18 años.
contadorPromedio_ = 0
sumarEdades = 0

for z in range(20):
    edades_ = int(input('Por favor ingrese las edades: '))
    if edades_ > 18:
        sumarEdades = sumarEdades + edades_
        contadorPromedio_ += 1

promedioEdades_ = sumarEdades / contadorPromedio_
print(f'El promedio de edades  es de: {promedioEdades_}')

# Hacer un programa que solicite 20 números y luego emitir por pantalla el
# máximo de los números pares y el mínimo de los números impares.
maxPar_ = 0
minImpar_ = 0

for m in range(20):
    parOImpar = int(input('Ingrese  numeros: '))
    if parOImpar % 2 == 0:
        if parOImpar > maxPar_:
            maxPar_ = parOImpar
    else:
        if parOImpar < minImpar_:
            minImpar_ = parOImpar

print(f' El maximo de los numeros pares es {maxPar_} y el minimo de los impares es {minImpar_}')


# Hacer un programa para ingresar 10 números y luego calcule y emita el mayor
# de los primos de la lista. En caso de no haber ningún número primo, deberá
# aclararlo con un cartel.