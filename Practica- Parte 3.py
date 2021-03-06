# LOTES DE CARGA Y PROCESOS   --------------------------------------------------------------
# 1. Una empresa que fabrica 20 artículos tiene la siguiente información para cada uno de ellos:
#       - Código de Artículo (4 dígitos, no correlativos).
#       - Precio Unitario.
# Este primer lote no se encuentra ordenado.
# Cuenta por otro lado con un lote de registros con las ventas del año anterior. Cada registro contiene
# la siguiente información:
#       - Número de Cliente (1 a 300).
#       - Código de Artículo (4 dígitos no correlativos).
#       - Mes (1 a 12).
#       - Día (1 a 31).
#       - Cantidad vendida.
# Puede haber más de un registro para el mismo artículo. El lote finaliza con un registro con número
# de cliente igual a cero.
# Se pide:
#   a) Un listado con el siguiente formato:
#       Código de Artículo 999
#       Cantidad Total Vendida 999
#   Este listado debe salir ordenado de mayor a menor por cantidad total vendida.
#   b) Informar, si los hubiera, los nombres de los meses en que no hubo ventas.
#   c) Informar los códigos de los artículos cuyas ventas en cantidad son mayores al promedio.
codigo1 = []
precio1 = []

for x in range(20):
    numcodigo1 = int(input('Ingrese el numero de codigo (4 digitos): '))
    numPrecio1 = float(input('Ingrese el precio del producto: $ '))
    codigo1.append(numcodigo1)
    precio1.append(numPrecio1)

accCantTotalVend = []

for d in range(20):
    accCantTotalVend.append(0)

mes = []

abc = 0
for a in range(12):
    m_ = abc + 1
    mes.append(m_)
    abc += 1

accVentMes = []

for r in range(12):
    accVentMes.append(0)

soliNumCliente = int(input('Ingrese el numero de cliente: '))
soliCodArticulo = int(input('Ingrese el codigo del articulo  (4 digitos): '))
solMes = int(input('Ingrese el mes (del 1 al 12): '))
solDia = int(input('Ingrese el dia (del 1 al  31): '))
solCantVend = int(input('Ingrese la cantidad: '))

while soliNumCliente != 0:
   for k in range(20):
        if soliCodArticulo == codigo1[k]:
            accCantTotalVend[k] += solCantVend
        if solMes == mes[k]:
            accVentMes[k] += solCantVend

   soliNumCliente = int(input('Ingrese el numero de cliente: '))
   soliCodArticulo = int(input('Ingrese el codigo del articulo  (4 digitos): '))
   solMes = int(input('Ingrese el mes (del 1 al 12): '))
   solDia = int(input('Ingrese el dia (del 1 al  31): '))
   solCantVend = int(input('Ingrese la cantidad: '))

# Metodo de la burbuja:
i = 0
while i < len(accCantTotalVend):
    j = i + 1
    while j < len(accCantTotalVend):
        if accCantTotalVend[i] < accCantTotalVend[j]:
            aux = accCantTotalVend[i]
            accCantTotalVend[i] = accCantTotalVend[j]
            accCantTotalVend[j] = aux
            aux = codigo1[i]
            codigo1[i] = codigo1[j]
            codigo1[j] = aux
        j += 1
    i += 1

z = 0
for g in range(5):
    print(f'''
Código de Artículo: {codigo1[z]}
Cantidad Total Vendida: {accCantTotalVend[z]}''')
    z += 1

mesSinVentas = []
mesNombre = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
             'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

auxMes = 0

for v in range(12):
    if accVentMes[v] == 0:
        mSinVent = mesNombre[v]
        mesSinVentas.append(mSinVent)
        auxMes = 1

if auxMes == 1:
    print(f'Los meses sin ventas fueron: {mesSinVentas}')
else:
    print(f'Hubo ventas todos los meses')

sumValoresArticulo = 0
for j in accCantTotalVend:
    sumValoresArticulo += j

promVenArticulos = sumValoresArticulo / len(accCantTotalVend)
print(promVenArticulos)

ind_ = 0
for art in accCantTotalVend:
    if art > promVenArticulos:
        print(f'El articulo {codigo1[ind_]}, supera el promedio de ventas ({promVenArticulos}), con {art} ventas.')
    ind_ += 1

# 2. Se dispone de un lote de 300 registros (uno por artículo), cada uno de los cuales tiene la
# siguiente información:
#       - Número de artículo (4 dígitos no correlativos).
#       - Cantidad de unidades en stock.
#       - Precio Unitario.
# El lote está desordenado.
# Se dispone de otro lote de registros, cada uno de los cuales corresponde a una venta con la siguiente
# información:
#       - Número de cliente (1 a 300).
#       - Número de artículo (4 dígitos, no correlativos).
#       - Cantidad de unidades vendidas.
# El último registro de este lote tiene número de cliente cero y no debe procesarse. Desarrollar el
# programa que determine e imprima:
#   a) Un listado de las ventas realizadas, con el siguiente formato:
#   Listado de ventas
#       Nro. Cliente        99
#       Nro.Artículo        99
#       Cantidad Vendida    999
#       Importe Total       999.99
#   b) Informar cuál es el número de cliente que más compró en total (en pesos).
#   c) Informar cada uno de los números de los artículos que no hayan registrado ventas.
numArt2 = []
cantUnidStock = []
precioUnit = []

for q in range(300):
    nA2 = int(input('Ingrese el numero de articulo (4 digitos): '))
    cUS2 = int(input('Ingrese la cantidad de unidades en stock del articulo: '))
    pU2 = float(input('Ingrese el precio del articulo: $ '))
    numArt2.append(nA2)
    cantUnidStock.append(cUS2)
    precioUnit.append(pU2)

numCliente2 = int(input('Ingrese el numero de Cliente: '))
numeroArticulo = int(input('Ingrese el numero de articulo (4 digitos): '))
cantUnidVendidas2 = int(input('Ingrese la cantidad de unidades vendidas: '))

nCli2 = []
accCantVen2 = []
impClien2 = []

for lu in range(300):
    accCantVen2.append(0)

indi_2 = 0
while numCliente2 != 0:
    indi_2 = 0
    for nr in numArt2:
        if numeroArticulo == nr:
            importeAAbonar2 = precioUnit[indi_2] * cantUnidVendidas2
            print(f'''Listado de ventas:
            Nro. Cliente:       {numCliente2}
            Nro.Artículo:       {numeroArticulo}
            Cantidad Vendida:   {cantUnidVendidas2}
            Importe Total:      ${importeAAbonar2}
            ''')
            nCli2.append(numCliente2)
            accCantVen2[indi_2] += cantUnidVendidas2
            impClien2.append(importeAAbonar2)
        indi_2 += 1
    numCliente2 = int(input('Ingrese el numero de Cliente: '))
    numeroArticulo = int(input('Ingrese el numero de articulo (4 digitos): '))
    cantUnidVendidas2 = int(input('Ingrese la cantidad de unidades vendidas: '))

maxPago = impClien2[0]
clienteMasPago = nCli2[0]

for d in range(len(impClien2)):
    if maxPago < impClien2[d]:
        maxPago = impClien2[d]
        clienteMasPago = nCli2[d]

print(f'El cliete que mas pago es el numero: {clienteMasPago}, con un monto de ${maxPago} ')

for w in range(len(accCantVen2)):
    if accCantVen2[w] == 0:
        print(f' El articulo numero {numArt2[w]}, no registro ventas')

# 3. Una empresa de transporte de carga por camión posee 20 tarifas distintas de acuerdo al destino
# de los envíos que deba realizar. Dispone de un lote de registros con la siguiente información:
#       - Número de Tarifa (Número de 4 cifras, no correlativos).
#       - Importe por KM.
# Este lote no viene ordenado. A continuación, dispone de un segundo lote de registros con la
# información de los envíos que se realizaron durante la semana pasada, conteniendo cada uno de
# ellos los siguientes campos:
#       - Número de Camión (1 a 100).
#       - Número de Tarifa.
#       - Kilómetros Recorridos.
# Este lote finaliza con un registro con número de camión negativo. Se nos pide realizar un programa
# que determine e informe:
#   a) El total recaudado por cada tarifa.
#   b) Un listado como el siguiente:
#       Número de camión    xxx
#       Total recaudado     xxx
vecNumTarifa3 = []
vecImpXKm = []

def cargarLote1(v1, v2, tam):
    for h in range(tam):
        a_ = int(input('Ingrese el numero de tarifa: '))
        b_ = float(input('Ingrese el importe por KM: $ '))
        v1.append(a_)
        v2.append(b_)

cargarLote1(vecNumTarifa3, vecImpXKm, 20)

def inicializarEn0(vector, tam):
    for b in range(tam):
        vector.append(0)

vectorNumCamion = []
vectorKilometrosRecorridosSegunTarifa =[]
vectorKmPorCamion = []
vectorTarifaCamion =[]

inicializarEn0(vectorKilometrosRecorridosSegunTarifa, 20)

numCamion = int(input('Ingrese el numero de camion(del 1 al 100): '))
numTarifaIngresado = int(input('Ingrese el numero de tarifa: '))
kilometrosRecorridos = float(input('Ingrese los kilometros recorridos: '))

while numCamion > 0:
    vectorNumCamion.append(numCamion)
    vectorKmPorCamion.append(kilometrosRecorridos)
    vectorTarifaCamion.append((numTarifaIngresado))
    for e in range(len(vecNumTarifa3)):
        if numTarifaIngresado == vecNumTarifa3[e]:
            vectorKilometrosRecorridosSegunTarifa[e] = kilometrosRecorridos
    numCamion = int(input('Ingrese el numero de camion(del 1 al 100): '))
    numTarifaIngresado = int(input('Ingrese el numero de tarifa: '))
    kilometrosRecorridos = float(input('Ingrese los kilometros recorridos: '))

def totalrecaudado():
    for t in range(len(vecNumTarifa3)):
        totalRecaud = vecImpXKm[t] * vectorKilometrosRecorridosSegunTarifa[t]
        print(f'Para la tarifa {vecNumTarifa3[t]} se recaudo un total de ${totalRecaud}')

totalrecaudado()

def listado(v9, v8):
    c = 0
    while c < len(vectorTarifaCamion):
        d = c
        while d < len(vecNumTarifa3):
            if vectorTarifaCamion[c] == vecNumTarifa3[d]:
                auxPrecio = vecImpXKm[d]
                e = 0
                while e < len(v9):
                    totalRecaudadoCamion = v8[e] * auxPrecio
                    print(f'''
                    Numero de camion:   {v9[e]}
                    Total recaudado:    ${totalRecaudadoCamion}
                    ''')
                    e += 1
            d += 1
        c += 1

listado(vectorNumCamion, vectorKmPorCamion)

#4.  Una empresa que realiza transporte de productos frágiles cuenta con una flota de 30 camiones.
# Se generó un lote de registros con los siguientes datos para cada camión:
#       - Número de camión (1 a 30).
#       - Código de chofer (3 dígitos, no correlativos).
# Este lote se encuentra ordenado por número de camión en forma ascendente (de menor a mayor).
# Cada código de chofer maneja uno y solo un camión.
# Existe un segundo lote con la información de los viajes realizados por los camiones en el mes de
# anterior, cada registro contiene:
#       - Día (1 a 31).
#       - Código de chofer (3 dígitos, no correlativos).
#       - Cantidad de kilómetros recorridos en ese viaje (entero).
#       - Cantidad de piezas rotas en ese viaje (entero).
# Este lote finaliza con un registro con día igual a cero. Se generó un registro por cada viaje realizado,
# por lo tanto, puede haber más de un registro para el mismo día y para el mismo código de chofer.
# Se pide determinar e informar:
#   a) Para cada día del mes informar cual fue el código de chofer que haya totalizado menor
#   cantidad de piezas rotas en un solo viaje. Tener en cuenta que los choferes que no realizaron
#   viajes ese día, no deben ser considerados.
#   b) Informar cual es el número de camión con el que se hayan recorrido mayor cantidad total de
#   kilómetros en el mes COMPLETO y que código de chofer lo conduce.
#   c) Informar para cada código de chofer el promedio de roturas entre todos los viajes realizados
#   en la primera quincena (día 1 a 15) y los realizados en la segunda quincena (día 16 a 31). El
#   formato será:
#   Código de chofer    999
#   Promedio Q1         999
#   Promedio Q2         999
vectorNumCamion4 = []
vectorCodigoChofer4 = []

def cargarLote4(v1, v2, tam):
    for h in range(tam):
        a_ = int(input('Ingrese el numero de Camion (el 1 al  30): '))
        b_ = float(input('Ingrese el codigo de chofer(3 digitos): '))
        v1.append(a_)
        v2.append(b_)

cargarLote4(vectorNumCamion4, vectorCodigoChofer4, 30)

def ordenAscendente(vecAOrdenar):
    h = 0
    while h in range(len(vecAOrdenar)):
        k = h +1
        while k < len(vecAOrdenar):
            if vecAOrdenar[k] < vecAOrdenar[h]:
                aux_numCa = vecAOrdenar[h]
                vecAOrdenar[h] = vecAOrdenar[k]
                vecAOrdenar[k] = aux_numCa
            k += 1
        h += 1

ordenAscendente(vectorNumCamion4)
ordenAscendente(vectorCodigoChofer4)

vectorDia = []
vectorKmViaje_ = []
vectorPiezasRotas = []
vectorCantidadViajes_chofer = []

inicializarEn0(vectorCantidadViajes_chofer, 30)

def cargarlote5():
    dia_ = int(input('Ingrese el dia: '))
    cod_chofer = int(input('Ingrese el codigo de chofer: '))
    cant_kmRecorridos = float(input('Ingrese la cantidad de km recorridos: '))
    cant_piezasRotas = int(input('Cantidad de piezas rotas: '))
    while dia_ != 0:
        vectorDia.append(dia_)
        vectorKmViaje_.append(cant_kmRecorridos)
        vectorPiezasRotas.append(cant_piezasRotas)
        cont_er = 0
        for efg in vectorCantidadViajes_chofer:
            if efg == cod_chofer:
                vectorCantidadViajes_chofer[cont_er] += 1
                cont_er += 1
            cont_er += 1
        dia_ = int(input('Ingrese el dia: '))
        cod_chofer = int(input('Ingrese el codigo de chofer: '))
        cant_kmRecorridos = float(input('Ingrese la cantidad de km recorridos: '))
        cant_piezasRotas = int(input('Cantidad de piezas rotas: '))

cargarlote5()

menor_cantViajes = vectorCantidadViajes_chofer[0]

#for dia in vectorDia:

# 5. Una empresa de alquiler de autos cuenta con distintas agencias desde donde efectúa sus
# operaciones. Para ello cuenta con varios lotes de registros. Un primer lote contiene los datos de los
# autos, cada registro está compuesto por:
#       - Código de auto (4 dígitos no correlativos).
#       - Categoría del auto (1 a 10).
#       - Importe del alquiler por km.
#       - Número de agencia (1 a 20).
# Este lote se encuentra ordenado por código de auto y contiene 400 registros.
# Existe un segundo lote con la información de los alquileres que se realizaron durante el mes pasado.
# Cada registro contiene:
#       - Código de auto (4 dígitos no correlativos).
#       - Número de cliente que efectúo el alquiler (1 a 200).
#       - Total de días del alquiler.
#       - Kms. Recorridos.
# Este lote finaliza con un registro con número de cliente igual a cero. Puede haber más de un registro
# para el mismo auto y para el mismo cliente.
# Por último, un tercer lote contiene los datos de las agencias de esta empresa.
#       - Número de agencia (1 a 20).
#       - Ubicación de la agencia (1=Aeropuerto Ezeiza, 2=Aeroparque, 3=Centro Ciudad).
# A partir de estos lotes se pide determinar e informar:
#   a) Un listado con el siguiente formato:
#       Número de Cliente   99
#       Total de pesos abonados en alquiler 999
#   b) La recaudación total acumulada para cada una de las tres ubicaciones.
#   c) La cantidad total de autos para cada una de las veinte agencias.
#   d) La categoría de auto más veces alquilada por los clientes.
#   e) Los números de las agencias, si las hubiera, que hayan efectuado en el mes menos de diez
#   alquileres en total. Para calcular el importe del alquiler de un auto se debe multiplicar el
#   importe en pesos por kilómetro por la cantidad de kilómetrosrecorridos.

# xxxxxxxxxxxxxxxxXX   ---------------------------------------------------------------------------