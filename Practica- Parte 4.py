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

# xxxxxxxxxxxxxxxxXX   ---------------------------------------------------------------------------