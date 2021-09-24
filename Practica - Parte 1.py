# Hacer un programa que permita ingresar por teclado dos números y que luego
# muestre por pantalla la suma, la resta, la multiplicación, la división, modulo y exponente
# de dichos números. Se deben mostrar los resultados en pantalla. Los números deben
# ser solicitados una única vez.

valor1 = int(input('Por favor ingrese el primer valor: '))
valor2 = int(input('Por favor ingrese el segundo valor: '))

#Suma:
suma = valor1 + valor2
print(f'El resultado de la suma es: {suma}')
#Resta:
resta = valor1 - valor2
print(f'El resultado de la resta es: {resta}')
#Multiplicación:
multiplicacion = valor1 * valor2
print(f'El resultado de la multiplicación es : {multiplicacion}')
#División:
division = valor1 / valor2
print(f'El resultado de la división es: {division}')
#Modulo:
modulo = valor1 % valor2
print(f'El modulo es: {modulo}')
#Exponente:
exponente = valor1 ** valor2
print(f'Resultado de la potencia es: {exponente}')

#Promedio de 4 calificaciones de un estudiante:

calificacion1 = int(input('Ingrese el resultado de la primer calificación: '))
calificacion2 = int(input('Ingrese el resultado de la segunda calificación: '))
calificacion3 = int(input('Ingrese el resultado de la tercera calificación: '))
calificacion4 = int(input('Ingrese el resultado de la cuarta calificación: '))

sumaCalificaciones= calificacion1 + calificacion2 + calificacion3 + calificacion4
promedio = sumaCalificaciones / 4
print(f' El promedio total es de: {promedio} ')

#Convertir unidades, de toneladas a libras:

valorToneladas = float(input('Ingrese el valor en Toneladas: '))
toneladasAKg = valorToneladas * 1000
valorLibras = toneladasAKg * 2.2
print(f'El resultado es: {valorLibras} libras.')

#Calcular el area y el perimetro de un rectangulo:

alto = float(input('Por favor ingrese el valor del alto en metros: '))
ancho = float(input('Por favor ingrese el valor del ancho en metros: '))
perimetro = alto * 2 + ancho * 2
superficie = alto * ancho
print(f'El valor del perimetro es {perimetro} metros y el valor de la superficie es {superficie} m2')

#El usuario ingresa el año actual y el año de la fecha de su
# nacimiento. Calcular y emitir la edad

aActual = int(input('Por favor ingrese  el año actual: '))
fechaNacimiento = int(input('Por favor ingrese el año de su nacimiento: '))
edad = aActual - fechaNacimiento
print(f'La edad es: {edad}')

#Hacer un programa que permita ingresar los kilómetros existentes entre dos
# ciudades y la velocidad promedio de un vehículo. Calcular y emitir por pantalla
# el tiempo aproximado que demandará llegar de un punto a otro teniendo en
# cuenta los datos ingresados.

distanciaCiudades = float(input(' Ingrese la distancia entre las dos ciudades (en Km): '))
velocidadPromedio = float(input(' Ingrese la velocidad promedio del automovil (en Km/h): '))
tiempoEstimado = velocidadPromedio // distanciaCiudades
print(f'El tiempo aproximado para llegar es de {tiempoEstimado} hs.')

# Una casa de computación paga a sus empleados un sueldo fijo de ARS15000,
# más una comisión del 5% sobre el total facturado por cada empleado. Hacer un
# programa para ingresar el total facturado por un empleado y que luego calcule
# y emita por pantalla el sueldo total a cobrar por el mismo.

sueldoFijo = 15000
comision = float(input('Ingrese el porcentaje de comision: '))
subtotal = (sueldoFijo * comision) / 100
sueldoTotal = sueldoFijo + subtotal
print(f'El sueldo total que incluye la comision del 5% es de ${sueldoTotal}')

# Hacer un programa para ingresar por teclado los metros cuadrados totales de
# un predio y los metros cuadrados cubiertos; luego calcular y mostrar por
# pantalla el porcentaje de metros cuadrados cubiertos y el porcentaje de
# metros cuadrados descubiertos.

superficieTerreno = float(input('Ingrese la superficie del lote en m2 :'))
superficieCubierta = float(input('Ingrese  la superficie cubierta en m2: '))
superficieDescubierta = superficieTerreno - superficieCubierta
porcentajeCubierto = (superficieCubierta * 100)/ superficieTerreno
porcentajeDescubierto = (superficieDescubierta * 100)/ superficieTerreno
print(f' El porcentaje de metros cubiertos es del {porcentajeCubierto}% y descubiertos es {porcentajeDescubierto}%')

# Una importante cadena de delivery cuenta con una promoción por tiempo
# limitado en la que otorga un 15% de descuento sobre el total del valor de la
# compra realizada. Hacer un programa para solicitar el monto total y el mismo
# calcule y emita por pantalla el total a cobrar con el descuento aplicado y el monto del descuento.

valorCompra = float(input('Ingrese el valor de la compra: '))
descuento = valorCompra *0.15
totalACobrar = valorCompra - descuento
print(f'El descuento es de ${descuento} y el monto total a abonar con el descuento incluido es de ${totalACobrar}')

# Una universidad desea conocer los porcentajes de mujeres y hombres en las
# carreras de ciencias exactas. Se solicita un programa para cargar la cantidad de
# mujeres y la cantidad de hombres y que el mismo calcule y emita por pantalla
# los porcentajes correspondientes.

cantidadHombres = int(input('Ingrese la cantidad de hombres: '))
cantidadMujeres = int(input('Ingrese la cantidad de mujeres: '))
porcentajeHombres = (cantidadHombres * 100) / (cantidadMujeres + cantidadHombres)
porcentajeMujeres = (cantidadMujeres * 100) / (cantidadMujeres + cantidadHombres)
print(f'El porcentaje de hombres incriptos es de {porcentajeHombres}% y de mujeres {porcentajeMujeres}%')

#-------------------------------------------------------------------------------------------------------------------
#Determinar  cual de los dos valores es el mayor

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero'))

if numero1 > numero2:
    print(f'El primer numero es el mayor, {numero1} ')
elif numero1 == numero2:
    print('Los numeros son iguales')
else:
    print(f'El segundo número es el mayor, {numero2}')


#Determinar si el valor ingresado es Par o  Impar:

valorNumerico = int(input('Ingrese un valor numerico:'))

if valorNumerico % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')