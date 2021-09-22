#aumentar valor de  2 en 2, hasta llegar al  250:

contador = 0

while contador <= 250:
    print('El valor es: ', contador)
    contador += 2
else:
    print('Fin del ciclo ')


#Es necesario pedir el titulo y el autor
#preguntarle al usuario los datos
#devolve el valor del usuario

titulo = input('Cual es el titulo del libro ?')
autor = input('Quien fue el autor del libro ?')
print(titulo, 'fue escrito por', autor)