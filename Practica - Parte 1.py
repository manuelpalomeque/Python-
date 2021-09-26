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
print(f'El porcentaje de hombres inscriptos es de {porcentajeHombres}% y de mujeres {porcentajeMujeres}%')

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

# Hacer un programa para ingresar un número y luego se emita un cartel por
# pantalla “Positivo” si el número es mayor a cero, “Negativo” si el número es
# menor a cero o “Cero” si el número es igual a cero.

numeroEvaludo = int(input('Ingrese el valor numerico a evaluar: '))

if numeroEvaludo > 0 :
    print(f'El número {numeroEvaludo}, es positivo')
elif numeroEvaludo < 0:
    print(f'El número {numeroEvaludo}, es negativo')
else:
    print(f'El número {numeroEvaludo}, es cero y por lo tanto es neutro')

# Una casa de video juegos otorga un descuento dependiendo del importe de la
# compra realizada según los siguientes valores:
# • Si el importe es menor a ARS 1000, no hay descuento.
# • Si el importe es ARS 1000 o más pero menor a ARS 5000, aplica un
# descuento del 10%.
# • Si el importe es ARS 5000 o más, aplica un descuento del 18%.

importeCompra = float(input('Ingrese el monto de la compra: '))
importeConDescuento = None

if importeCompra < 1000:
    print(f'El monto es inferior a lo solicitado, por ende no hay descuento. Monto a abonar: ${importeCompra}')
elif importeCompra >= 1000 and importeCompra < 5000:
    importeConDescuento = importeCompra * 0.90
    print(f' Se aplica un descuento del 10%. El monto a abonar es de ${importeConDescuento} ')
elif importeCompra >= 5000:
    importeConDescuento = importeCompra * 0.82
    print(f'Se aplica un descuento del  18%. El monto a abonar es de $ {importeConDescuento}')

# Hacer un programa para ingresar un valor que estará expresado en minutos. Si
# los minutos superan los 60, pasar el valor a horas, de lo contrario dejarlo en
# minutos. Mostrar el resultado en pantalla aclarando si se muestran minutos u
# horas.

minutos = int(input('Ingresar la cantidad en minutos: '))
valorEnHs = None

if minutos >= 60:
    valorEnHs = minutos / 60
    print(f' El resultado en horas es de {valorEnHs} hs')
else:
    print(f'No es necesario pasar a horas. El resultado en minutos es {minutos}')

#Rango a establecer entre 0 a 5. Informar si esta dentro del rango

valorIngresado = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5
dentroDeRango = (valorIngresado >= valorMinimo) and (valorIngresado <= valorMaximo)

if dentroDeRango:
    print('Esta dentro de rango')
else:
    print('no esta dentro del rango')

#El usuario debe ingresar el mes en el que esta y el programa le debe indicar la
#estacion

mes = int(input('ingrese un mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Invierno'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Primavera'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Verano'
elif mes == 10 or mes == 10 or mes == 12:
    estacion = 'Otoño'
else:
    print('ingrese un valor dentro del rango del  1 al 12')

print(f'Para el mes {mes} , la estacion es {estacion}')

# Hacer un programa que solicite el ingreso de un número y que luego emita un
# cartel por pantalla aclarando si el mismo es múltiplo de 5.
numMultiplo = int(input('Ingrese el valor a consultar: '))

if numMultiplo % 5 == 0:
    print(f'El numero {numMultiplo} es multiplo de 5')
else:
    print(f'El numero {numMultiplo} no es multiplo de 5')

# Hacer un programa que solicite el ingreso de dos números y luego calcular:
# a. La resta si el primero es mayor que el segundo.
# b. La suma si son iguales.
# c. El producto si el primero es menor.
# Se deberá emitir un cartel por pantalla con el resultado correspondiente.

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
resultado = None

if num1 > num2:
    resultado = num1 - num2
    print(f' Se efectuo la resta de los numeros y el resultado es: {resultado}')
elif num1 == num2:
    resultado = num1 + num2
    print(f'Se efectuo una suma, el resultado es {resultado}')
else:
    resultado = num1 * num2
    print(f'Se calculo el producto, el resultado es {resultado}')

# Hacer un programa para ingresar dos números. Si el segundo es distinto de
# cero, calcular la división del primero por el segundo y mostrar el resultado por
# pantalla; caso contrario, emitir un cartel aclarando que no se puede dividir por
# cero.
valor_1 = int(input('Ingrese el primer numero: '))
valor_2 = int(input('Ingrese el segundo numero: '))
resul = None

if valor_2 != 0:
    resul = valor_1 / valor_2
    print(f'El resultado de la division es {resul}')
else:
    print('No se puede dividir por cero')

# Un importante negocio de desinfectante líquido realiza descuentos
# dependiendo de la cantidad de litros vendidos según la siguiente escala:
# a. Si vende menos de 100 litros, no hay descuento.
# b. Si vende entre 101 y 300 litros, el descuento es del 10%.
# c. Si vende entre 301 y 500 litros, el descuento es del 15%.
# d. Finalmente, si la venta es de más de 500 litros, el descuento es del 25%.
# Hacer un programa que solicite el ingreso del importe total de la venta y la
# cantidad de litros vendidos y calcule y emita el importe con el descuento
# aplicado.

cantidadLitrosVendidos = float(input('Ingrese la cantidad de litros vendidos: '))
montoSinDescuento = float(input('Ingrese el monto a cobrar: '))
totalAbonar = None

if cantidadLitrosVendidos <= 100:
    print(f'No se aplica descuento, debe abonar ${montoSinDescuento}')
elif cantidadLitrosVendidos > 100 and cantidadLitrosVendidos <= 300:
    totalAbonar = montoSinDescuento * 0.9
    print(f'Se aplica un descuento del  10% y el monto a cobrar es ${totalAbonar}')
elif cantidadLitrosVendidos > 300 and cantidadLitrosVendidos < 500:
    totalAbonar = montoSinDescuento * 0.85
    print(f'Se aplica descuento del  15% y el monto a abonar es de ${totalAbonar}')
else:
    totalAbonar= montoSinDescuento * 0.75
    print(f'Se aplica un descuento del 25% y el monto a abonar es de ${totalAbonar}')

#  Hacer un programa para ingresar por teclado la longitud de los tres lados de un
# triángulo y que luego determine e informe con un cartel aclaratorio a qué tipo
# de triángulo corresponde:
# a. Equilátero: cuando los tres lados sean iguales.
# b. Isósceles: cuando dos de los tres lados sean iguales.
# c. Escaleno: cuando todos los lados sean distintos.

long1 = float(input('Ingrese la longuitud del primer lado: '))
long2 = float(input('Ingrese la longuitud del segundo lado: '))
long3 = float(input('Ingrese la longuitud del tercer lado: '))

if long1 == long2 and long1 == long3:
    print('El triangulo es equilatero, tiene sus tres lados iguales ')
elif long1 == long2 or  long2 == long3 or long3 == long1:
    print('El triangulo es isóceles, dos de sus lados son iguales')
else:
    print('El triangulo es escaleno, ninguno de sus lados son iguales')