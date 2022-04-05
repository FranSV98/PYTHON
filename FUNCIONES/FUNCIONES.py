#Include

import random


#Funciones

def areaCirculo(radio):
    area = 3.14 * (radio**2)
    return area

def numeroAleatorio (minimo,maximo): 
    a = random.randint(0, maximo)
    return a

def suma (x,y):
    return x+y 

def listaNumAleatorios (tama,minimo,maximo):
    lista  = []
    for i in range (tama):
        lista.append (random.randint (minimo,maximo))
    return lista

#EJERCICIOS

#Area circulo : pi*r2
def funcionCirculo ():
    radio= int(input("Introduce el radio de tu circunferencia: "))
    area = areaCirculo (radio)
    print (area)

#Numero aleatorio
def funcionAleatorio ():
    aleatorio= numeroAleatorio (0,100)
    print (aleatorio)

#Suma
def funcionSuma ():
    a = int(input ("introduce un numero: "))
    b = int(input ("Introduce un numero: "))
    c = suma (a,b)
    print (c)



#Ejecutable

#funcionCirculo ()
#funcionAleatorio ()
#funcionSuma ()

print (listaNumAleatorios (3, 0 ,100))



