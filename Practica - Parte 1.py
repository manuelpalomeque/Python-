#Calculadora: Pedirle al usuario que ingrese dos valores y emplear los operadores
#arigmeticos en ellos.

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


#Califica tu dia del  1 al  10
#preguntarle al usuario como estuvo su dia
#devolve el valor del usuario

resultadoDia = int(input('Del 1 al 10, Como estuvo tu dia ?'))
print('Mi dia estuvo de :', resultadoDia)

#Es necesario pedir el titulo y el autor
#preguntarle al usuario los datos
#devolve el valor del usuario

titulo = input('Cual es el titulo del libro ?')
autor = input('Quien fue el autor del libro ?')
print(titulo, 'fue escrito por', autor)

#convertir unidades, de toneladas a libras:

valorToneladas = float(input('Ingrese el valor en Toneladas: '))

toneladasAKg = valorToneladas * 1000
valorLibras = toneladasAKg * 2.2

print(f'El resultado es: {valorLibras} libras.')

#Calcular el area y el perimetro de un rectangulo:
alto = int(input('Por favor ingrese el valor del alto'))
ancho = int(input('Por favor ingrese el valor del ancho'))

perimetro = alto * 2 + ancho * 2
superficie = alto * ancho

print(f'El valor del perimetro es: {perimetro} y el valor de la superficie es {superficie}')

#Determinar si el valor ingresado es Par o  Impar:

valor = int(input('Ingrese un valor numerico:'))

if valor % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')