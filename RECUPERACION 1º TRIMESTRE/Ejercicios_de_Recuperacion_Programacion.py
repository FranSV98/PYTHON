#Recuperación Programacion


import random
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista.insert(i, random.randrange(0, 1000, 2))
      return lista


#4
def impcad(x):
    print (x)

#5
def saludo (nom):
    print ("Saludos",nom)
#11
def implistdeb (l):
    for l in list:
        print(l)
#12
def implist(l):
    print(*l)
#13
def listconcomas (l):
    print (*l ,sep=",", end=",")
    
#14
def listend (l):
    print (*l ,sep=",", end=".")
#15
def numlet (x):
    list(x)
    a=len(x)
    print(a)
    
#16
def mayus (x):
    print(x.upper())

#17
def minus (x):
    print(x.lower())


#18
def titulo (x):
    print(x.title())
#19
def delreves(x):
    print ((x)[::-1])
#20
def palin (x):
    if str(x) == str(x)[::-1] :
        print("Palindromo")
    else:
        print("No Palindromo")

#--------------------------------------------------------------------

#1
#print ("¡Hola!")

#2
#x= "¡Hola!"
#print (x)

#3
#nm= (input("Escriba un nombre"))
#print (('¡Hola ' + nm +'!') *4)

#4
#n= "Voy a casa"
#impcad (n)

#7
#nom= (input ("Su nombre"))
#saludo (nom)

#9
#a=0
#while a<10:
    #palabras= (input("Escriba diez palabas"))
    #a+=1
#list(palabras)

#10
#pala= input("Escriba palabras")
#while pala!="salir":
 #   pala= input("Escriba palabras")
#else:
 #   pala="salir"
#    print ("Ha salido del programa")
    

#11
#lista= ["Azul","Amarillo","Verde","Rojo"]
#implistdeb (lista)

#12
#lista= ["Azul","Amarillo","Verde","Rojo"]
#implist (lista)

#13
#lista= ["Azul","Amarillo","Verde","Rojo"]
#listconcomas(lista)

#15
#ad=(input("Introduce una palabra"))
#numlet(ad)

#16
#tm=(input("Introduzca una palabra"))
#mayus (tm)


#17
#minu=(input("Introduzca una palabra"))
#minus (minu)



#18
#titu=(input("Introduzca una palabra"))
#titulo (titu)

#19
#alrev=(input("Introduzca una palabra"))
#delreves (alrev)

#20
#word = (input("Escribe una palabra para comprobar si es palindromo"))
#palin(word)

#21
#n=int(input("Ingrese cuantos numeros aleatorios desea obtener"))
#aleatorios=listaAleatorios(n)
#print(aleatorios)

#22
#n=int(input("Ingrese un numero para comprobar si es par o impar"))
#if n%2==0:
 #   print ("Es par")
#else:
#     print ("Es impar")

#23
##n=int(input("Ingrese un numero "))
##for i in range(n-1,-1,-1):
##    print (i)

#24
##a=int(input("Ingrese un numero "))
##for x in range(0, a, 2):
##    print(x)
##for x in range(0, a, -2):
##  print(x)

#25
##lista_numeros= [2,3,4,5,6,7,8,9,23,56,78,-22]  
##numero_par = []
##numero_impar = []
##for i in lista_numeros:
##    if i % 2 == 0:
##        numero_par.append(i)
##    else:
##        numero_impar.append(i)
##    
##print (("Numeros pares"),numero_par)
##print (("Numeros impares"),numero_impar)

#27
##lista_numeros= [2,3,4,5,6,7,8,9,23,56,78,-22]
##x=sum(lista_numeros)
##print(x)

#28
##lista_numeros= [2,3,4,5,6,7,8,9,23,56,78,-22]
##x=sum(lista_numeros)
##y=len(lista_numeros)
##print (x%y)

#29
##nota = float(input("Introduce la nota"))
##if (nota == 10):
##    print ("Matrícula de Honor")
##elif (nota >= 9):
##    print ("Sobresaliente")
##elif (nota >= 7):
##     print ("Notable")
##elif (nota >= 6):
##    print ("Bien")
##elif (nota >= 5):
##    print ("Aprobado")
##
##else:
##    print ("Suspenso")
##if (nota >= 7):
##    print ("Enhorabuena")


#30
##lista2= []
##n=int(input("Ingrese un numero "))
##while n>=0:
##    lista2.append(n)
##    n=int(input("Ingrese un numero "))
##else:
##    x=sum(lista2)
##    y=len(lista2)
##    print ("Su nota media es")(x%y)

#31 incomleto
asignaturas= []
lista2= []
a=0
b=0
while a!=5:
    asig= input("Escriba sus asignaturas")
    asignaturas.append(asig)
    a+=1
    
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?"))
    if nota<0:
        x=sum(lista2)
        y=len(lista2)
        print ("Su nota media es", (x%y))

    else:
        lista2.append(nota)


#34




    
