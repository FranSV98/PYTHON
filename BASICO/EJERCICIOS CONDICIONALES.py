#EJERCICIO 1
print ("\n EJERCICIO 1------>")


edad = int(input("¿Que edad tienes?:"))
if edad < 18:
    print ("Eres menos de edad.")
else:
    print ("Eres mayor de edad.")

#EJERCICIO 2
print ("\n EJERCICIO 2------>")

cadena = "contraseña"
contraseña = input("¿Cual es la contraseña?:")
if cadena == contraseña.lower():
    print ("La contraseña coincide")
else :
    print ("La contraseña no coincide")

#EJERCICIO 3
print ("\n EJERCICIO 3------>")

dividendo = float(input("Introduce el dividendo:"))
divisor = float(input("Introduce el divisor:"))
if divisor == 0:
    print ("No se puede dividir por 0")
else:
    print (dividendo/divisor)

#EJERCICIO 4
print ("\n EJERCICIO 4------>")

numero = int(input("Introduce un numero:"))
if numero % 2==0:
    print ("El numero %s es par" % (numero))
else:
    print ("El numero %s es impar" % (numero))

#EJERCICIO 5
print ("\n EJERCICIO 5------>")

edad = int(input("¿Que edad tienes?:"))
ingresos = float(input("¿Cuales son tus ingresos mensuales?:"))
if edad > 16 and ingresos >= 1000:
    print ("Tienes que cotizar")
else:
    print ("No puedes cotizar")

    
#EJERCICIO 6
print ("\n EJERCICIO 6(ES COPIADO)------>")

nombre = input("Introduce tu nombre:")
sexo = input("Introduce tu sexo:")

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"

else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Tu grupo es " + grupo)
    

#EJERCICIO 7
print ("\n EJERCICIO 7(ES COPIADO)------>")

renta = float(input("¿Cual es tu renta anual?"))

if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
print ("Tienes que pagar ",renta*tipo / 100, "€", sep='')


#EJERCICIO 8
print ("\n EJERCICIO 8(ES COPIADO)------>")
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))

if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = ("Meritorio")
else:
    nivel = ""

if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))


#EJERCICIO 9
print ("\n EJERCICIO 9------>")
edad = int(input("¿Cuale es tu edad?"))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10
print ("La entrada cuesta", precio, "€")


#EJERCICIO 10
print ("\n EJERCICIO 10(COPIADO)------>")

# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")

# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")



