# print ("Hola mundo")

#entero = 2
#print ("entero que no es entero")
#print (entero)

#decimal = 2.25
#print ("decimal")
#print (decimal)

#entero = 2.0
#print ("entero que no es entero")
#print (entero)

#entero = "dos"
#print ("entero escrito")
#print (entero)



#no = "I don't like"
#print(no)
#si = 'Me parece "bien"'
#print(si)



#uno, dos = 1, 2
#tres = uno + " " + dos
#print(tres)
#solucion = uno - dos
#print(solucion)

#uno, dos = "1", "2"
#tres = uno + " " + dos
#print(tres)

#hola = "hola"
#mundo = "mundo"
#print(hola + " " + mundo)

#lista = [1,2,3]
#print (lista)
#print (lista [1])
#print (lista [10])
#lista.append(4)

#for elemento in lista:
#    print (elemento)

#for x in lista:
#    print (x)

#suma = 1 + 2
#print (suma)
#resta = 2 - 1
#print (resta)
#mult = 2 * 3.0
#print (mult)
#div = 5 / 2
#print (div)

#num = 5
#num = num + 2
#print (num)
#num += 2
#print (num)










###30.9.2021###

#nombre = "Celia"
#edad = "veinticinco"
#print ("Hola " + nombre)
#print ("Hola, soy " + nombre + " y tengo " + edad + " años.")
#edad = 25
#print ("Hola, soy %s." % nombre)
#print ("Hola, soy %s y tengo %d años." % (nombre, edad))



#lista = [1,2,3]
#print (lista)
#print ("Tengo una lista: %s" % lista)
#print ("Tengo una lista: %s" % lista[2])    #FEO
#print ("Tengo una lista: %d" % lista[2])

#num = 2.568947
#print ("Este es mi número: %f" % num)
#print ("Este es mi número: %.2f" % num)

#nom = "Celia"
#print (len (nom))

#print (nom.index("C"))
#print (nom.index("e"))
#print (nom.index("l"))
#print (nom.index("i"))
#print (nom.index("a"))

#palabra = "abecedario"
#print (palabra.index("e"))     # Primera ocurrencia de la letra
#print (palabra.count("be"))    # Número de veces que aparece

#print (palabra[3:7])
#print (palabra.upper())

#print (palabra)
#palabra = palabra.upper()  # Escribe en mayúscula.
#print (palabra)
#palabra = palabra.lower()  # Escribe en minúscula.
#print (palabra)

#print (palabra.startswith("abe"))   # Indica si empieza así la palabra.
#print (palabra.endswith("rio"))   # Indica si acaba así la palabra.

#frase = "Esto ya no es el abecedario"
#print (frase.split(" "))    #Separa la cadena en una lista cada vez que aparezca el caracter indicado.
#print (frase.split("a"))





#1.10.2021# #CONDICIONES#

#num = 2
#print ("Numero es igual a 2")
#print (num == 2)
#print ("Numero es igual a 3")       
#print (num == 3)
#print ("Numero es mayor que uno")     
#print (num > 1)
#print ("numero es menos que uno")
#print (num < 1)
#print ("numero es distinto a dos")
#print (num != 2)
#print ("numero es distinto a tres")
#print (num != 3)

#num = 5
#print ("Numero es igual a cinco:")
#resultado = (num == 5)
#print (resultado)
#if resultado == True:
#        print ("verdadero")
#if (num ==5):
#    print ("Verdadero")
#else:
#    print ("Falso")


#nota = 5
#if (nota >= 9):
#    print ("Sobresaliente")----------#if (Si x es mayor que x)
#elif (nota >= 7):
#    print ("Notable")
#elif (nota >= 6):
#    print ("Bien")
#elif (nota >= 5):
#    print ("Aprobado")
#elif (nota >= 5):
#    print ("Aprobado")
#else:
#    print ("Suspenso")


# primera_fila = ["Marco", "Joel"]
# name = "Marco"
# if name in primera_fila:
#     print ("Esta en primera fila")
# else:
#     print ("No esta en primera fila")

# if name in ["Marco", "Joel"]:
#     print ("Esta en la primera fila")
# else:
#     print ("No esta en primera fila")

# if nota > 5 and nota < 7:
#     print ("Enhorabuena")
#     print ("Pero tienes que trabajar mas")






#BUCLES#

#primos = [2,3,5,7]
#for primo in primos:
#    print (primo)

#nombres = ["Marco", "Joel","Pablo","Javi","Vicky"]
#for nombre in nombres:
#    print (nombre)
#for nombre in nombres:
#    for letra in nombre:
#        print (letra)
#    print ("")
#print ("FIN")


#for x in range (5):
#    print (x)

#for x in range (0,5):
#    print (x)

#lista = []
#print (lista)
#for x in range (10):
#    lista.append(x)
#print (lista)


#lista =[]
#num = 5
#while num < 7.0:
#    lista.append(num)
#    num += 0.5
#print (lista)

#for x in lista:          #Esto hace que escriba para abajo
#    print (x)



lista = []
num = 5.0
while num < 10:
    lista.append(round(num,1))  #Pone todos los decimales de los valores que le indiques (5.1, 5.2, 5.3 etc)
    num += 0.1
print (lista)

for x in lista:
    print (x)










 






