#aumentar valor de  2 en 2, hasta llegar al  250:

contador = 0

while contador <= 250:
    print('El valor es: ', contador)
    contador += 2
else:
    print('Fin del ciclo ')

# iterar un rango de 0 a 10 e imprimir numeros divisibles
# entre 3

for i in range(10):
    if i % 3 == 0:
        print(i)
else:
    print('Fin del ciclo')

