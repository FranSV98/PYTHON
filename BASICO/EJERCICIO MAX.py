#EJERCICIO MAX


##import random
##
##lista = []                                    ##Lista con numeros aleatorios
##for n in range (20):
##    lista.append(random.randint(0,20))
##print (lista)




##import random
##
##lista = []
##for n in range (20):
##    lista.append(random.randint(0,20))        ##Imprime el maximo y el minimo
##maximo = max(lista)
##minimo = min(lista)
##print (lista)
##print (maximo)
##print (minimo)



##import random
##
##lista = []
##for n in range (20):
##    lista.append(random.randint(0,20))            ##Saca el numero maximo de la lista
##maximo = lista[0]
##for n in lista:
##    if n > maximo:
##        maximo = n
##print (lista)
##print (maximo)



#EJERCICIO LEN(Cuenta cuantos caracteres tiene la frase)

##frase = "El perro de san roque no tiene rabo"
##print (len(frase))


##frase = "El perro de san roque no tiene rabo"
##contador = 0
##for c in frase:
##    contador+=1
##print (contador)


##Contar cuantas vocales y consonantes tiene

##frase= "El perro de san roque no tiene rabo"
##contV= 0
##contC= 0
##contE= 0
##for i in frase:
##    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":                  #Contador vocales y consonantes
##        contV+= 1
##    elif i == " ":
##        contE += 1
##    else:
##        contC += 1
##print (contV)
##
##print (contC)





#Ejercicio invertir cadena

##frase = "el perro de san roque no tiene rabo"
##nuevaFrase = ""
##for i in frase:                                     #Invertir cadena sin funciones ni nada
##    nuevaFrase = i + nuevaFrase
##print (nuevaFrase)






#EJERCICIO PALINDROMOS

##frase = ("sugus")
##nuevaFrase = ""
##for i in frase:
##    nuevaFrase = i + nuevaFrase                     #Saber si es palindromo
##if nuevaFrase == frase: 
##    print ("Palindromo")
##print (nuevaFrase)






#Quitar espacios

   
##frase = "el perro de san roque no tiene rabo"
##nuevaFrase = ""
##for i in frase:                                   #Quitar espacios
##    if i != " ":
##        nuevaFrase += i
##print (nuevaFrase)
##





#Convertir numero en string sin usar str

##num = int(input("Introduce el numero"))
##num1 = f"{num}"                                     #convertir a string sin usar str
##print (num1 + "hola")







#Encontrat una palabra

##print("\nEjercicio 7 - Palabra en frase")
##
##frase = input("Escribe una frase: ")
##palabra = input("Escribe una palabra: ")
##posicion = 1
##
##frase = frase.split()
##
##for i in frase:
##    if palabra in i:
##        print('La palabra "' + palabra + '" se encuentra en la posición ' + str(posicion))
##    posicion += 1













