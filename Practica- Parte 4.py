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
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self.edad = edad

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
        print(f'Persona: {self._nombre}, {self._apellido}. {self.edad} años')

persona1 = Persona('Jonathan', 'Palomeque', 30)

print(f'Objeto Persona 1: {persona1._nombre}, {persona1._apellido}, {persona1.edad}')
Persona.mostrar_detalle(persona1)

# Crear una clase para generar diferentes tipos de automoviles de una agencia de ventas.Encapsular e implementar
# los metodos GET y SET en todos los atributos (marca, color, antiguedad).
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

# Heredar las caracteristicas de la clase padre "Persona", que se pasa a la clase hijo "Empleados".
# Agregar el atributo sueldo
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, sueldo): # sin esta linea va a dar error
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

    def mostrar_detalle(self):
        print(f'''Empleado: 
    Nombre: {self._nombre}
    Apellido: {self._apellido} 
    Edad: {self.edad} años
    Sueldo: ${self.sueldo}
    ''')

empleado1 = Empleado('Juan', 'Paez', 28, 50000)
Empleado.mostrar_detalle(empleado1)

# Definir la clase padre "Vehiculo" con los atributos: color y ruedas, encapsular e implementar
# los metodos get y set. Crear las clases hijas:
# 1) Coche:
#       Agregar el atributo "velocidad". Encapsular e implementar metodos
# 2) Bicicleta:
#       Agregar el atributo "tipo". Encapsular e implementar metodos
class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return  self._ruedas
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color}, ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f'''Coche:
        {super().__str__()}, velocidad: {self._velocidad} km/hr'''

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return  f'''Bicicleta: 
        {super().__str__()}, tipo: {self._tipo}'''

coche1 = Coche('azul', 'cuatro tipo A', 100)
print(coche1)

bicicleta1 = Bicicleta('rojo', 'dos tipo C', 'montaña')
print(bicicleta1)

#Crear una clase Videojuegos, la cual permita tener un contador  ID de numero de videojuego
class Videojuego:
    contador_juego = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_juego += 1
        return cls.contador_juego

    def __init__(self, nombre, plataforma):
        self.id_juego = Videojuego.generar_siguiente_valor()
        self.nombre = nombre
        self.plataforma = plataforma

    def __str__(self):
        return f'Videojuego [{self.id_juego} {self.nombre} {self.plataforma}]'


juego1 = Videojuego('Pokemon', 'Nintendo')
juego2 = Videojuego('Mario Bross', 'Nintendo')
juego3 = Videojuego('Mortal Kombat', 'Play Station')

print(f'''Valor Contador total de videojuegos: {Videojuego.contador_juego}
    Juego: {juego1.nombre}
    Contador: {juego1.id_juego}

    Juego: {juego2.nombre}
    Contador: {juego2.id_juego}

    Juego: {juego3.nombre}
    Contador: {juego3.id_juego}
    ''')

# POLOMORFISMO:
# Crear una clase hija de la clase "Empleado" (desarrollada en los primeros ejercicios), la cual
# se llamara "Gerente" y cuenta con los atributos: nombre, sueldo y departamento.
# Aplicar el concepto de polimorfismo.

class Gerente(Empleado):
    def __init__(self, nombre, apellido, edad, sueldo, departamento):
        super().__init__(nombre,apellido, edad, sueldo)
        self.departamento = departamento

    def __str__(self):
        return  f'Gerente: Departamento {self.departamento}, {super().__str__()}'

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado1 = Empleado('Juan', 'Paez',30, 5000)
imprimir_detalles(empleado1)

print('-'.center(50, '-'))

gerente1 = Gerente('Carla', 'Maciel', 29, 20000, 'Sistemas' )
imprimir_detalles(gerente1)

# Laboratorio Mundo PC:
# A)Crear la clase padre "DispositivoEntrada" con los atributos: tipoEntrada y marca. Aplicar encapsulamiento
# y metodos get y set
class DipositivoEntrada:

    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada
    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        print(f'Caracteristicas: {self._tipoEntrada} y {self._marca}')

# B)Crear la clase hija "Raton" con los atributos: marca y tipoEntrada. Incorporar la
# variable de clase"contadorRatones. Aplicar encapsulamiento.
class Raton(DipositivoEntrada):
    contadorRatones = 0

    def __init__(self, marca, tipoEntrada):
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f' ID : {self._idRaton}, marca: {self._marca}, tipo Entrada: {self._tipoEntrada}'

# C)Crear la clase hija "Teclado" con los atributos: marca y tipoEntrada. Incorporar la
# variable de clase"contadorTeclados. Aplicar encapsulamiento.
class Teclado(DipositivoEntrada):

    contadorTeclados = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f' ID: {self._idTeclado}, marca: {self._marca}, tipo de entrada: {self._tipoEntrada}'

# D)Crear la clase "Monitor" con los atributos: marca y tamaño. Incorporar la
# variable de clase"contadorMonitores. Aplicar encapsulamiento y metodos Get y Set.
class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    @property
    def idMonitor(self):
        return  self._idMonitor
    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return  self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    def __str__(self):
        return f'ID: {self._idMonitor}, marca: {self._marca},tamaño: {self._tamaño} Pulgadas'

# E)Crear la clase "Computadora" con los atributos: nombre, referencias de objetos: monitor, teclado
# y raton. Incorporar la variable de clase "contadorComputadoras". Aplicar encapsulamiento y metodos
# Get y Set.
class Computadora:

    contadorComputadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadora += 1
        self._idComputadora =  Computadora.contadorComputadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return  self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return  self._teclado
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton
    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
        Id: {self._idComputadora} 
        Nombre: {self._nombre}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

# xxxxxxxxxxxxxxxxXX   ---------------------------------------------------------------------------