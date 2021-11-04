# CLASES   --------------------------------------------------------------------------------------

# Crear una clase para realizar operaciones de sumar, restar, etc.
class Aritmetica:

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar_3(self):
        return  self.operandoA + self.operandoB

    def restar_3(self):
        return  self.operandoA - self.operandoB

    def multiplicar_3(self):
        return  self.operandoB * self.operandoB

    def dividir_3(self):
        return  self.operandoA / self.operandoB

aritmetica1 = Aritmetica(4, 5)

print(f'El resultado de la suma es {aritmetica1.sumar_3()}')
print(f'El resultado de la resta es {aritmetica1.restar_3()}')
print(f'El resultado de la multiplicacion es {aritmetica1.multiplicar_3()}')
print(f'El resultado de la dicision es {aritmetica1.dividir_3():.2f}')

# Crear una clase para calcular el área de un rectángulo.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return  self.base * self.altura

base = float(input('Por favor ingrese la dimension de la base: '))
altura = float(input('Por favor ingrese el valor de la altura: '))

rectangulo1 = Rectangulo(base, altura)

print(f'El área del rectángulo es: {rectangulo1.calcular_area():.2f} m2')

# Crear una clase para calcular el volumen de un rectángulo.
class Cubo:
    def __init__(self, largoCubo, anchoCubo, profundidadCubo):
        self.largo = largoCubo
        self.ancho = anchoCubo
        self.profundidad = profundidadCubo

    def calcular_volumen(self):
        return  self.largo * self.ancho * self.profundidad

largoCubo = float(input('Ingrese el Largo: '))
anchoCubo = float(input('Ingrese el ancho: '))
profundidadCubo = float(input('Ingrese la profundidad: '))

cubo1 = Cubo(largoCubo, anchoCubo, profundidadCubo)
print(f'El volumen total es: {cubo1.calcular_volumen():.2f} m3')

# Crear una clase para generar diferentes tipos de personas de una agenda.Implementar los metodos
#GET y SET en el atributo nombre. Definir el atributo apellido como "Read Only"
class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre}, {self._apellido}. {self.edad}  {self.valores} {self.terminos}')

persona1 = Persona('Jonathan', 'Palomeque', 30, '4848906', 2, 3, m='manzana', p= 'pera')

print(f'Objeto Persona 1: {persona1._nombre}, {persona1._apellido}, {persona1.edad}')
Persona.mostrar_detalle(persona1)

# Crear una clase para generar diferentes tipos de automoviles de una agencia de ventas.Implementar los metodos
#GET y SET en todos los atributos (marca, color, antiguedad).
class Auto:
    def __init__(self, marca, color, antiguedad):
        self._marca = marca
        self._color = color
        self._antiguedad = antiguedad

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def antiguedad(self):
        return self._antiguedad
    @antiguedad.setter
    def antiguedad(self, antiguedad):
        self._antiguedad = antiguedad

    def mostrar_detalle(self):
        print(f'''Automovil: 
    Marca: {self._marca}
    Color: {self._color} 
    Antiguedad: {self._antiguedad} años
    ''')

auto1 = Auto('Fiat', 'Rojo', 10)
Auto.mostrar_detalle(auto1)

# xxxxxxxxxxxxxxxxXX   ---------------------------------------------------------------------------