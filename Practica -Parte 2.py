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

# Hacer un programa para mostrar los números del 10 al 1. No se debe realizar
# ningún pedido de datos. USANDO WHILE.
cont1_ = 10

while cont1_ >= 1:
    print(cont1_)
    cont1_ -= 1

# Hacer un programa que solicite la edad de un grupo de personas. El programa
# deberá pedir edades hasta que se ingrese una edad menor a 18 años. Deberá
# mostrar por pantalla cuántas personas mayores se registraron.
contPerMayores = 0
edad = int(input('Ingrese la edad: '))

while edad >= 18:
    contPerMayores += 1
    edad = int(input('Ingrese la edad: '))
else:
    print(f'La contidad de personas mayores de 18 años es {contPerMayores}')

# Hacer un programa que solicite dos números y luego muestre los números
# entre el menor y el mayor de ellos. Acordate, usando While.
n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))

if n1 > n2:
    mayor_ = n1
    menor_ = n2
else:
    mayor_ = n2
    menor_ = n1
while menor_ < mayor_:
    print(menor_)
    menor_ += 1

# Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.
con_primos = 0
vueltas_primos = 1

v1 = int(input('Ingrese el valor a evaluar: '))

while vueltas_primos <= v1:
    if v1 % vueltas_primos == 0:
        con_primos += 1
    vueltas_primos += 1

if con_primos == 2:
    print('El numero es primo')
else:
    print('El numero no es primo')

# Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego mostrar por pantalla el máximo de ellos y la posición
# en la que fue ingresado.
number = int(input('Por favor ingrese el numero: '))
contNumber = 0
maxNumber = None

while number != 0:
    if contNumber == 0:
        maxNumber = number
    elif number > maxNumber:
        maxNumber = number
    contNumber += 1
    number = int(input('Por favor ingrese el numero: '))
else:
    print(f'El numero mas grande es {maxNumber} y se ingreso en la posicion {contNumber}')

# Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego mostrar por pantalla el menor y el segundo menor.
#además indicar la posición en la que fue encontrado cada uno de los mínimos.
number_ = int(input('Por favor ingrese el numero: '))
pGlobal = 0
minNumber1_ = None
minNumber2_ = None
pMin1 = 0
pMin2 = 0

while number_ != 0:
    if pGlobal == 0:
        minNumber1_ = number_
        pMin1 += 1
        pGlobal += 1
    elif number_ < minNumber1_:
        minNumber2_ = minNumber1_
        minNumber1_ = number_
        pMin2 = pMin1
        pMin1 = pGlobal
    number_ = int(input('Por favor ingrese el numero: '))
    pGlobal += 1
else:
    print(f'El numero menor es {minNumber1_} y se ingreso en la posicion {pMin1}, el segundo menor es {minNumber2_} '
          f'y se ingreso en la posicion {pMin2}')

# Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego emitir por pantalla el máximo de los números
# negativos y el mínimo de los números positivos.
ban_ = 0
maxNeg = 0
minPos = 0
num_ingresados = int(input('Ingrese el numero: '))

while num_ingresados != 0:
    if ban_ == 0:
        if num_ingresados > 0:
            minPos = num_ingresados
        else:
            maxNeg = num_ingresados
        ban_ += 1
    elif minPos == 0 or maxNeg == 0:
        if minPos == 0 and num_ingresados > 0:
            minPos = num_ingresados
        elif maxNeg == 0 and num_ingresados < 0:
            maxNeg = num_ingresados
    if num_ingresados < 0 and num_ingresados < maxNeg:
        maxNeg = num_ingresados
    if num_ingresados >= 1 and num_ingresados < minPos:
        minPos = num_ingresados
    num_ingresados = int(input('Ingrese el numero: '))
else:
    print(f'El maximo de los numeros negativos es {maxNeg} y el minimo de los positivos es {minPos}')

# Hacer un programa para ingresar una lista de números que corta cuando se
# ingresa un cero y luego mostrar: la cantidad de números primos, la cantidad de
# números pares, la cantidad de positivos y la cantidad de negativos.
cantPri_ = 0
cantPares_ = 0
cantPositv_ = 0
cantNega_ = 0
nIngresado_ = int(input('Ingrese el numero: '))

while nIngresado_ != 0:
    if nIngresado_ > 0:
        cantPositv_ += 1
    else:
        cantNega_ += 1
    if nIngresado_ % 2 == 0:
        cantPares_ += 1
    contPri_ = 0
    c = 1
    while c <= nIngresado_:
        if nIngresado_ % c == 0:
            contPri_ +=1
        c += 1
    if contPri_ == 2:
        cantPri_ += 1
    nIngresado_ = int(input('Ingrese el numero: '))
else:
    print(f'''La cantidad de: 
            numeros primos: {cantPri_},
            numeros pares: {cantPares_},
            numeros positivos: {cantPositv_},
            numeros negativos: {cantNega_}''')

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
        posicionMinimo = x + 1
else:
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

#FUNCIONES -----------------------------------------------------------------------------

# Hacer una función llamada “producto” que reciba dos números enteros y que
# devuelva el producto de ambos. Luego hacer un programa que pida el precio
# de un artículo y la cantidad vendida y muestre por pantalla el monto total a
# pagar. Usar la función.
def producto(nu1, nu2):
    return  nu1 * nu2

preProduc = float(input('Ingrese el precio del producto: '))
cantVen = int(input('Ingrese la cantidad de productos: '))

monTot = producto(preProduc, cantVen)
print(f'El monto total es ${monTot}')

# Hacer una función llamada “mayor” que reciba dos números enteros y
# devuelva el mayor de ellos o cero si son iguales.
def mayor(v_n1, v_n2):
    if v_n1 > v_n2:
        return v_n1
    elif v_n1 == v_n2:
        return 0
    else:
        return v_n2

no1 = int(input('Ingrese el primer valor: '))
no2 = int(input('Ingrese el segundo valor: '))
res_ = mayor(no1, no2)
print(res_)

# Hacer una función llamada “par” que reciba un número entero y devuelva 1 si
# es par o cero si no lo es. Hacer un programa para ingresar 20 números y
# mostrar por pantalla cuántos son pares.

# Hacer una función llamada “primo” que reciba un número entero y devuelva 1
# si el número es primo o cero si no lo es. Hacer un programa para ingresar
# números. El lote corta cuando se ingresa un número cero. Informar el
# promedio teniendo en cuenta sólo los números primos.

# Hacer una función llamada “pagos” que reciba un monto (float) y una cantidad
# de pagos (entero) y devuelva el monto de cada pago. Hacer un programa para
# ingresar 10 ventas. Para cada venta se conoce el monto y la cantidad de pagos.
# El programa deberá mostrar la cantidad de pagos y el monto del pago para
# cada una de las ventas.

# Hacer una función que se llame “sumaResta” que reciba dos números y que
# devuelva la suma Y la resta del primer número con el segundo.
# Nota: recordemos que una función solo puede devolver UN valor por return.
# Cómo podríamos hacer para tener ambos resultados en el main?

# Hacer una función de tipo void (porque no va a devolver nada) llamada
# “positivoNegativoCero” que reciba un número por valor y una variable por
# referencia. Que analice el número y escriba variable recibida por referencia
# con:
# a. 1 si el número es positivo.
# b. -1 si el número es negativo.
# c. 0 si el número es cero.

# Hacer un programa main que permita ingresar 100 números y emitir por
# pantalla cuántos son positivos, cuántos negativos y cuántos cero.

# Hacer un programa que permita ingresar una lista de números que corta
# cuando se ingresa un cero. A partir de dichos datos informar:
# a. El mayor de los números pares.
# b. La cantidad de números impares.
# c. El menor de los números primos.
# Hacer uso de las funciones anteriormente desarrolladas.

# Filtrar las comidas que no sean carne
# Encuentra y devuelve la gallina
# Dime donde esta la gallina
# Rellenar la lista de dinero
# esta bien?
# Hay algun error?


#LISTAS     ----------------------------------------------------------------------------
# Dada la siguiente tupla, crear una lista que sólo incluya
# los números menor que 5 utilizando un ciclo for.
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for t in tupla:
    if t < 5:
        lista.append(t)
else:
    print(f'Los numeros menores de 5 son: {lista}')

# Transformar cada numero  de la lista que se formo en el el ejercicio anterior
# , multiplicandolo por 2

for o in range(len(lista)):
    lista[o] = lista[o] * 2
else:
    print(f'El resultado de los valores de la lista multiplicado por 2 es: {lista}')

# Hacer un programa para ingresar cinco números distintos, formar una lista,
# y luego mostrar por pantalla el mayor y el menor de ellos.
lista1_ = []
x = 0

while x in range(5):
    num_lista1_ = int(input('Ingrese el numero: '))
    lista1_.append(num_lista1_)
    x += 1
else:
    print(f'El valor mayor es {max(lista1_)} y el menos es {min(lista1_)}')

# Hacer un programa para ingresar cuatro números, formar una lista
# y luego mostrar por cuáles son mayores a 100.
lista2_ = []
q = 0

for q in range(4):
    numb_lista2 = int(input('Ingrese el numero: '))
    lista2_.append(numb_lista2)
    q += 1

def mayor100(nume):
    return (nume > 100)

numeros_mayores = list(filter(mayor100, lista2_))
print(f'los numeros mayores a 100 son: {numeros_mayores}')

# Hacer un programa para ingresar cuatro números, formar una lista
# y luego mostrar por cuántos son menores a 100.
list_3 = []
s = 0

for s in range(4):
    val_num = int(input('Ingrese el numero: '))
    list_3.append(val_num)
    s += 1

def menor100_(numer):
    return  numer < 100

menores_100 = list(filter(menor100_, list_3))
print(f'Los numeros menores a 100 son : {menores_100}')