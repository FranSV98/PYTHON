#Ejercicio 1
print ("Ejercicio 1------->")

print ("Hola Mundo")

#Ejercicio 2
print ("\nEjercicio 2------->")

cadena = "¡Hola Mundo!"
print(cadena)

#Ejercicio 3
print ("\nEjercicio 3------->")

nombre = input ("¿Como te llamas?")

print ("Hola %s" % (nombre))

#Ejercicio 4
print ("\nEjercicio 4------->")

print (((3 + 2) / (2 * 5)) **2)

#Ejercicio 5
print ("\nEjercicio 5------->")

horas = int(input("¿Cuantas horas trabajadas tienes?"))
cobro = float(input("¿Y a cuanto cobras las horas?"))
resultado = (horas * cobro)
print ("Tienes %d horas trabajadas y las cobras a %.2f €, en total has ganado %d €" % (horas, cobro,resultado))

#Ejercicio 6
print ("\nEjercicio 6------->")

n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

#Ejercicio 7
print ("\nEjercicio 7------->")

peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))

#Ejercicio 10
print ("\nEjercicio 10------->")

peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))


#Ejercicio 12
print ("\nEjercicio 12------->")

barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")
