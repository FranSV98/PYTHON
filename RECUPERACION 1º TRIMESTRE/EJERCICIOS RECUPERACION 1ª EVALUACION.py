import random
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista.insert(i, random.randrange(0, 1000, 2))
      return lista
#--------------------------------------------------------#
#                      FUNCIONES                         #
#--------------------------------------------------------#
def imprimirCadena(cad):
      return input(cad)

def solicitarFrase(nom):
      return input(nom)

def imprimirFrase(frase):
      return (frase)

def saludo (nom):
      print ("Saludos",nom)


def impCadena(nom):
      nombre = "Hola Paco"
      print (nombre)
      

def implistdeb (l):
      for l in lista:
            print(l)


def impLista(l):
      print(*l)


def listaConComas (l):
      print (*l ,sep=",", end=",")
    

def listaConY (l):
      print (*l ,sep=",", end=". \n")


def numlet (x):
      list(x)
      a=len(x)
      print(a)
    

def mayusculas (x):
      print(x.upper())


def minusculas (x):
      print(x.lower())


def titulo (x):
      print(x.title())


def alReves(x):
      print ((x)[::-1])


def esPalindromo (x):
      if str(x) == str(x)[::-1] :
            print("Palindromo")
      else:
            print("No Palindromo")

def esPrimo(num):
      num = ""
      if num<2:
            return False
      for i in range (2, num):
            if num % i == 0:
                  return False
      return True

    


#--------------------------------------------------------#
#                      CODIGO                            #
#--------------------------------------------------------#

#__EJERCICIO 1__#
print ("EJERCICIO 1--->")
print ("!HOLA¡ \n")

#__EJERCICIO 2__#
print ("EJERCICIO 2--->")

nombre = ("!HOLA¡\n")
print (nombre)

#__EJERCICIO 3__#
print ("EJERCICIO 3--->")
nombre = input("Introduce tu nombre:")

respuesta = ("¡Hola " + nombre + "!\n")
print (respuesta)

#__EJERCICIO 4__#
print ("EJERCICIO 4--->")
cadena = "Hola,esta es la primera funcion\n"
cad = cadena
print (cad)

#__EJERCICIO 5__#
print ("EJERCICIO 5--->")
frase = "Esta frase es una prueba\n"
nom = frase
print (nom)

#__EJERCICIO 6__#
print ("EJERCICIO 6--->")
frase = input("Introduce una frase:")
imprimirFrase = frase
print (frase)

#__EJERCICIO 7__#
print ("EJERCICIO 7--->")
nom= (input ("Escribe tu nombre:"))
saludo (nom)

#__EJERCICIO 8__#
print ("EJERCICIO 8--->")
print (impCadena(nom))

#__EJERCICIO 9__#
print ("EJERCICIO 9--->")
a=0
while a<10:
    palabras= (input("Escriba diez palabas:"))
    a+=1
list(palabras)

#__EJERCICIO 10__#
print ("EJERCICIO 10--->")
pala= input("Escriba una palabra:")
while pala!="salir":
    pala= input("Escriba una palabra:")
else:
    pala="salir"
    print ("Ya no esta en el programa")
    
#__EJERCICIO 11__#
print ("EJERCICIO 11--->")
lista= ["Azul","Amarillo","Verde","Rojo"]
implistdeb (lista)

#__EJERCICIO 12__#
print ("EJERCICIO 12--->")
lista= ["Azul","Amarillo","Verde","Rojo"]
impLista (lista)

#__EJERCICIO 13__#
print ("EJERCICIO 13--->")
lista= ["Azul","Amarillo","Verde","Rojo \n"]
listaConComas(lista)

#__EJERCICIO 14__#
print ("EJERCICIO 14--->")
lista= ["Azul","Amarillo","Verde","Rojo"]
listaConY(lista)
#__EJERCICIO 15__#
print ("EJERCICIO 15--->")
ad=(input("Escriba una palabra:"))
numlet(ad)

#__EJERCICIO 16__#
print ("EJERCICIO 16--->")
tm=(input("Escriba una palabra:"))
mayusculas (tm)

#__EJERCICIO 17__#
print ("EJERCICIO 17--->")
minu=(input("Escriba una palabra:"))
minusculas (minu)

#__EJERCICIO 18__#
print ("EJERCICIO 18--->")
titu=(input("Escriba una palabra:"))
titulo (titu)

#__EJERCICIO 19__#
print ("EJERCICIO 19--->")
alrev=(input("Escriba una palabra:"))
alReves (alrev)

#__EJERCICIO 20__#
print ("EJERCICIO 20--->")
palabra = (input("Escribe una palabra para comprobar si es palindromo:"))
esPalindromo(palabra)

#__EJERCICIO 21__#
print ("EJERCICIO 21--->")
n=int(input("Ingresa cuantos numeros aleatorios desea obtener:"))
aleatorios=listaAleatorios(n)
print(aleatorios)

#__EJERCICIO 22__#
print ("EJERCICIO 22--->")
n=int(input("Ingresa un numero para comprobar si es par o impar:"))
if n%2==0:
   print ("Es par")
else:
     print ("Es impar")
     
#__EJERCICIO 23__#
print ("EJERCICIO 23--->")
n=int(input("Ingresa un numero:"))
for i in range(n-1,-1,-1):
    print (i)

#__EJERCICIO 24__#
print ("EJERCICIO 24--->")
a=int(input("Ingresa un numero:"))
for x in range(0, a, 2):
    print(x)
for x in range(0, a, -2):
  print(x)
  
#__EJERCICIO 25__#
print ("EJERCICIO 25--->")
lista_numeros= [2,3,4,5,6,7,8,9,23,56,78,-22]  
numero_par = []
numero_impar = []
for i in lista_numeros:
    if i % 2 == 0:
        numero_par.append(i)
    else:
        numero_impar.append(i)
    
print (("Numeros pares"),numero_par)
print (("Numeros impares"),numero_impar)

#__EJERCICIO 26__#
print ("EJERCICIO 26--->")

#__EJERCICIO 27__#
print ("EJERCICIO 27--->")
lista_numeros= [2,3,4,5,6,7,8,9,23,56,78,-22]
x=sum(lista_numeros)
print(x)

#__EJERCICIO 28__#
print ("EJERCICIO 28--->")
lista_numeros= [2,3,4,5,6,7,8,9,23,56,78,-22]
x=sum(lista_numeros)
y=len(lista_numeros)
print (x%y)

#__EJERCICIO 29__#
print ("EJERCICIO 29--->")
nota = float(input("Introduce la nota:"))
if (nota == 10):
    print ("Matrícula de Honor")
elif (nota >= 9):
    print ("Sobresaliente")
elif (nota >= 7):
     print ("Notable")
elif (nota >= 6):
    print ("Bien")
elif (nota >= 5):
    print ("Aprobado")

else:
    print ("Suspenso")
if (nota >= 7):
    print ("Enhorabuena")
    
#__EJERCICIO 30__#
print ("EJERCICIO 30--->")
lista2= []
n=int(input("Ingresa un numero:"))
while n>=0:
    lista2.append(n)
    n=int(input("Ingresa un numero:"))
else:
    x=sum(lista2)
    y=len(lista2)
    print ("Su nota media es(x%y)")
#__EJERCICIO 31__#
print ("EJERCICIO 31--->")

#__EJERCICIO 32__#
print ("EJERCICIO 32--->")

#__EJERCICIO 33__#
print ("EJERCICIO 33--->")

#__EJERCICIO 34__#
print ("EJERCICIO 34--->")
numero= int(input("¿Qué número quieres saber si es primo? "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("El número no es primo" )
else:
  print("El numero es primo")

#__EJERCICIO 35__#
print ("EJERCICIO 35--->")

#__EJERCICIO 36__#
print ("EJERCICIO 36--->")

#__EJERCICIO 37__#
print ("EJERCICIO 37--->")

#__EJERCICIO 38__#
print ("EJERCICIO 38--->")

#__EJERCICIO 39__#
print ("EJERCICIO 39--->")

#__EJERCICIO 40__#
print ("EJERCICIO 40--->")












        
        
        

































    
    
