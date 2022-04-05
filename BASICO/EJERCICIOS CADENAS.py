#EJERCICIO 1
print ("Ejercicio 1 ------->")

nombre = input("¿Como te llamas?")
numero = int(input("Dime el numero:"))
print ((nombre + "\n")* numero)


#EJERCICIO 2
print ("\n Ejercicio 2 ------->")

nombre = input("¿Cual es tu nombre?")
nombre = nombre.lower()
print (nombre)
nombre = nombre.upper()
print (nombre)
nombre = nombre.title()
print (nombre)

#EJERCICIO 3
print ("\n Ejercicio 3 ------->")

nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

#EJERCICIO 4
print ("\n Ejercicio 4 ------->")

tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

#EJERCICIO 5
print ("\n Ejercicio 5 ------->")
 
def inversa():
  string=input("Escribe una frase: ")
  cadenaInvertida = string [:: - 1 ]
  print( cadenaInvertida )
inversa()


#EJERCICIO 6
print ("\n Ejercicio 6 ------->")
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))


#EJERCICIO 7
print ("\n Ejercicio 7 ------->")

correo = input("ingrese un correo: ")

correoNuevo = correo[:correo.find('@')] + '@idetel.com.ar'

print (correoNuevo)

#EJERCICIO 8
print ("\n Ejercicio 8 ------->")

precio = input("ingrese el precio con dos decimales: ")
cotiz = input("ingrese la cotizacion: ")

entero = precio[:precio.find('.')]
decimal = precio[precio.find('.')+1:]

print("el total es " + entero + "€ con: " + decimal + " centimos")

#EJERCICIO 9
print ("\n Ejercicio 9 ------->")
fecha = input ("ingrese la fecha en formato dd/mm/aaaa: ")

dia = fecha[:fecha.find('/')]
mesanio = fecha[fecha.find('/')+1:]

mes = mesanio[:mesanio.find('/')]
anio = mesanio[mesanio.find('/')+1:]

print("dia: " + dia)
print("mes: " + mes)
print("anio: " + anio)

#EJERCICIO 10
print ("\n Ejercicio 10 ------->")
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))

#EJERCICIO 11
print ("\n Ejercicio 11 ------->")

producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))

