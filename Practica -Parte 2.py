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
def par(number_123):
    if number_123 % 2 == 0:
        return 1
    else:
        return 0

contador_dePares = 0
numeroQuePido = int(input('Ingrese el valor numerico: '))

for g in range(20):
    if par(numeroQuePido) == 1:
        contador_dePares += 1
    g += 1
    numeroQuePido = int(input('Ingrese el valor numerico: '))
else:
    print(f'La cantidad de numeros pares es: {contador_dePares}')

# Hacer una función llamada “primo” que reciba un número entero y devuelva 1
# si el número es primo o cero si no lo es. Hacer un programa para ingresar
# números. El lote corta cuando se ingresa un número cero. Informar el
# promedio teniendo en cuenta sólo los números primos.
def primo(ent):
    acc = 0
    for x in range(1, ent + 1):
        if ent % x == 0:
            acc += 1
    if acc == 2:
        return 1
    else:
        return 0

entero_ = int(input('Ingrese el numero: '))
pNum_ = 0
con_primos = 0

while entero_ != 0:
    res_do = primo(entero_)
    if res_do == 1:
        pNum_ += entero_
        con_primos += 1
    entero_ = int(input('Ingrese el numero: '))
    res_do = 0
else:
    pro_pr = pNum_ // con_primos
    print(f'El promedio con los numeros primos es {pro_pr}')

# Hacer una función llamada “pagos” que reciba un monto (float) y una cantidad
# de pagos (entero) y devuelva el monto de cada pago. Hacer un programa para
# ingresar 10 ventas. Para cada venta se conoce el monto y la cantidad de pagos.
# El programa deberá mostrar la cantidad de pagos y el monto del pago para
# cada una de las ventas.
def pagos(mon, cuo):
    return mon / cuo

for m in range(10):
    monto_ = float(input('Ingrese el monto: $ '))
    cuotas_ = int(input('Ingrese la cantidad de cuotas: '))
    total_cuo = pagos(monto_, cuotas_)
    print(f'El monto total es de {monto_}, se abonara en {cuotas_} cuotas de ${total_cuo} cada una')

# Hacer una función llamada posNegCero” que reciba un número por valor y una variable por
# referencia. Que analice el número y escriba variable recibida por referencia
# con:
# a. 1 si el número es positivo.
# b. -1 si el número es negativo.
# c. 0 si el número es cero.
# Hacer un programa main que permita ingresar 100 números y emitir por
# pantalla cuántos son positivos, cuántos negativos y cuántos cero.
def posNegCero(n, j):
    if n == 0:
        j = 0
    elif n > 0:
        j = 1
    else:
        j = -1
    return  j

accPos = 0
accNeg = 0
accCero = 0
ban_dera = None

for f in range(5):
    n = int(input('Ingrese numero: '))
    ban_dera = posNegCero(n, ban_dera)
    if ban_dera == 0:
        accCero += 1
    elif ban_dera == 1:
        accPos += 1
    else:
        accNeg += 1
else:
    print(f'cantidad de positivos {accPos}, cantidad de negativos {accNeg}'
          f' y la cantidad de ceros {accCero}')

# Hacer un programa que permita ingresar una lista de números que corta
# cuando se ingresa un cero. A partir de dichos datos informar:
# a. El mayor de los números pares.
# b. La cantidad de números impares.
# c. El menor de los números primos.
# Hacer uso de las funciones anteriormente desarrolladas.
number_n = int(input('Ingrese el numero: '))
mayNum_pares = 0
accPrimos_0 = 0
menNum_impares = 0

while number_n !=0:
    if par(number_n) == 1:
        if mayNum_pares == 0:
            mayNum_pares = number_n
        elif number_n >mayNum_pares:
            mayNum_pares = number_n
    else:
        if menNum_impares == 0:
            menNum_impares = number_n
        elif number_n < menNum_impares:
            menNum_impares = number_n
    if primo(number_n) == 1:
        accPrimos_0 += 1
    number_n = int(input('Ingrese el numero: '))
else:
    print(f'El mayor de los pares es {mayNum_pares}, el menor de los impares es {menNum_impares}'
          f' y la cantidad de numeros primos es {accPrimos_0}')

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

# Hacer un programa que solicite 50 números enteros y los guarde en un vector.
# Luego recorrer el vector y determinar e informar cuál es la suma de los valores
# del mismo.
vector1 =[]

for d in range(50):
    num_vector1 = int(input('Ingrese el numero: '))
    vector1.append(num_vector1)
    d += 1

sumValVec = 0
for numerosVector in vector1:
    sumValVec += vector1[numerosVector]
else:
    print(f'La suma de los valores da un total de {sumValVec}')

# Hacer un programa que solicite 50 números enteros y los guarde en un vector.
# Luego recorrer todos los elementos del vector y determinar cuál es el valor
# máximo y su posición dentro del vector.
vector2 = []

for x1 in range(50):
    num_vector2 = int(input('Ingrese el numero: '))
    vector2.append(num_vector2)
    x1 += 1

contIndiceVector2 = 1
valMaxVector2 = vector2[0]
posValMaxV2 = 0

for v2 in vector2:
    if v2 > valMaxVector2:
        valMaxVector2 = v2
        posValMaxV2 = contIndiceVector2
    contIndiceVector2 += 1
else:
    print(f'El numero mayor es {valMaxVector2} y se ingreso en la posicion {posValMaxV2}')

# Hacer un programa que solicite 100 números enteros y los guarde en un
# vector. Luego recorrer ese vector para calcular el promedio. Mostrar por
# pantalla los valores del vector que son mayores al promedio calculado.
vector3 = []

for ab in range(100):
    numVector3 = int(input('Ingrese el valor: '))
    vector3.append(numVector3)

sumVector3 = 0
for v3 in vector3:
    sumVector3 += v3
promVector3 = sumVector3 / len(vector3)

vector3MayPro = []
for v3_ in vector3:
    if v3_ > promVector3:
        vector3MayPro.append(v3_)

print(f'El promedio es: {promVector3} y los valores mayores al promedio son: {vector3MayPro}')

# Dada una lista de 10 números enteros, cargarlos en un vector. Luego,
# determinar e informar si el vector está ordenado en forma creciente. Por
# ejemplo el vector con los valores 1, 3, 5, 7 y 9 está ordenado; el vector 1, 5, 3, 7
# y 9 no lo está.
vector4 = []

for bc in range(10):
    numVector4 = int(input('Ingrese el valor: '))
    vector4.append(numVector4)

banVector4 = 1
maxVector4 = vector4[0]

for v4 in vector4:
    if v4 >= maxVector4:
        maxVector4 = v4
    else:
        banVector4 = 0
        break

if banVector4 == 1:
    print(f'Los valores estan ordenados: {vector4}')
else:
    print(f'Los valores estan desordenados: {vector4}')

# Hacer un programa que solicite una serie de valores de tipo char (caracteres).
# Se entiende por carácter a cada elemento que se obtiene de presionar una
# tecla. Por ejemplo el valor “25” tiene dos caracteres (si quisiéramos guardarlo
# en variables enteras nos alcanza con una, pero si queremos guardarlo en
# variables char, necesitaremos dos); la frase “maxi programa” tiene 13 (se
# incluye el espacio como un carácter).
# La cantidad de valores será como máximo 50, pero el programa puede cortar
# antes si se ingresa el carácter “.” (punto). Una vez cargado el vector de char,
# recorrerlo y reemplazar todas las apariciones de la letra “a” por la letra “e”,
# por ejemplo:
# Vector char original: “Hola muchachada cómo están”.
# Vector char modificado: “Hole muchechede cómo esten”
# Finalmente, mostrar el resultado en pantalla.
# Nota: necesitaremos un vector char de 50, pero no lo cargaremos con un For.
vector5 =[]
cVector5 = input('Ingrese el caracter:')
pV = '.'

while cVector5 != pV and len(vector5) < 50:
    vector5.append(cVector5)
    cVector5 = input('Ingrese el caracter:')

letV5A = 'a'
contIndiV5 = 0

for v5 in vector5:
    if v5 == letV5A:
        vector5[contIndiV5] = 'e'
    contIndiV5 += 1
print(vector5)

# Dada una lista de 10 números, cargarlos en un vector. Luego detectar si en el
# vector hay algún elemento repetido. De haberlo, indicarlo con un cartel
# aclaratorio “Hay repetidos”, de lo contrario indicar “No hay repetidos”.
vector6 = []

for cd in range(10):
    numVector6 = int(input('Ingrese el numero: '))
    vector6.append(numVector6)

banderaV6 = 0

for v6 in vector6:
    repeV6 = v6
    contRepeV6 = 0
    for repeV6 in vector6:
        if repeV6 == v6:
            contRepeV6 += 1
    if contRepeV6 >= 2:
        banderaV6 = 1

if banderaV6 == 0:
    print('No hay repetidos')
else:
    print('Hay numeros repetidos')

# Una empresa comercializa 15 tipos de artículos y por cada venta realizada
# genera un registro con los siguientes datos:
# • Número de artículo (1 a 15).
# • Cantidad vendida.
# Puede haber varios registros para el mismo artículo y el último se indica
# número de artículo igual a cero.
# Se pide determinar e informar:
# a. El número de artículo que más se vendió en total.
# b. Los números de artículos que no registraron ventas.
# c. La cantidad de unidades vendidas para el artículo número 10.
# Nota: tener en cuenta el concepto de “registro” y el planteo de estructura
# principal separado de consignas (ver videos de ciclos combinados y ejercicios
# resueltos de ciclos combinados).
vector7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

numArticulo = int(input('Ingrese el numero de articulo(del 1 al 15): '))
cantVendida_ = int(input('Ingrese la cantidad vendida: '))

while numArticulo != 0:
    vector7[numArticulo-1] = vector7[numArticulo-1] + cantVendida_
    numArticulo = int(input('Ingrese el numero de articulo: '))
    cantVendida_ = int(input('Ingrese la cantidad vendida: '))

maxVector7 = vector7[0]
artVector7 = 1

for fg in range(15):
    if vector7[fg] >= maxVector7:
        maxVector7 = vector7[fg]
        artVector7 = fg + 1

indiceNoVendidos = []

for hi in range(15):
    if vector7[hi] == 0:
        indiceNoVendidos.append(hi+1)

print(f'Los articulos que no registraron ventas fueron: {indiceNoVendidos}')
print(f'El articulo que mas se vendio fue el {artVector7} con {vector7[artVector7-1]} unidades vendidas')
print(f'Cantidad de productos vendidos para el articulo 10 = {vector7[9]} productos')

# Se ingresa una lista de 20 números en un vector. Se pide ordenar dichos
# números en forma decreciente (de mayor a menor). Mostrar el listado
# ordenado.
vector8 = []

for jk in range(20):
    numVector8 = int(input('Ingrese el numero: '))
    vector8.append(numVector8)

vector8.sort()
print(vector8)
