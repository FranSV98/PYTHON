#EJERCICIO 1 --> Escribe un programa que pida dos numeros enteros e indique si son pares o impares.
print ("EJERCICIO 1------>Escribe un programa que pida dos numeros enteros e indique si son pares o impares.\n")


###Primer Metodo
##def esPar(num1):
##    return num1%2==0
##    return num2%2==0
##num1 = int(input("Introduce el primer numero:"))
##num2 = int(input("Introduce el segundo numero:"))
##if (esPar(num1)):
##    print ("El numero es par")
##else:
##    print ("El numero es impar")
##if (esPar(num2)):
##    print ("El numero es par")
##else:
##    print ("El numero es impar")



#Segundo Metodo(El de clase)
def par (numero):
    esPar = True
    if numero%2 != 0:
        esPar = False
    return esPar

x = int(input("Escribe el primer numero:"))
y = int(input("Escribe el segundo numero:"))
if par(x)==True:
    print ("Es par")
else:
    print ("Es impar")

if par(y)==True:
    print("Es par")
else:
    print("Es impar")




#EJERCICIO 2 -->Escribe un programa que pida dos números enteros y calcule la resta de los dos.
print ("\nEJERCICIO 2------>Escribe un programa que pida dos números enteros y calcule la resta de los dos.\n")
def restaNum(x,y):
    return x-y

x = int(input("Escribe el primer numero"))
y = int(input("Escribe el segundo numero"))
c = restaNum (x,y)
print (c)


#EJERCICIO 3 -->Escribe un programa que pida dos números enteros y calcule la suma de los dos.
print ("\nEJERCICIO 3------>Escribe un programa que pida dos números enteros y calcule la suma de los dos.\n")
def sumaNum(x,y):
    return x+y
x = int(input("Introduce el primer numero:"))
y = int(input("Introduce el segundo numero:S"))
c = sumaNum (x,y)
print (c)


#EJERCICIO 4 -->Escribe un programa que pida dos números enteros e indique si son positivos o negativos.
print ("\nEjercicio 4------>Escribe un programa que pida dos números enteros e indique si son positivos o negativos.\n")
def positivo (numero):
    esPositivo = True
    if numero <0:
        esPositivo = False
    return esPositivo

x = int(input("Escribe el primer numero:"))
y = int(input("Escribe el segundo numero:"))
if positivo(x)==True:
    print ("Es positivo")
else:
    print ("Es negativo")

if positivo(y)==True:
    print("Es positivo")
else:
    print("Es negativo")


#EJERCICIO 5 -->Escribe un programa que pida dos números enteros y calcule si la suma es positiva o negativa.
print ("\nEjercicio 5------>Escribe un programa que pida dos números enteros y calcule si la suma es positiva o negativa.\n")

def positivo (x,y):
    Esuma = True
    operacion = x + y
    if operacion <0:
        Esuma = False
    return Esuma
x = int(input("Escribe el primer numero:"))
y = int(input("Escribe el segundo numero:"))
if positivo(x,y)==True:
    print ("Es positivo")
else:
    print ("Es negativo")
    


#EJERCICIO 6 -->Escribe un programa que pida dos números enteros y calcule si la resta es positiva o negativa.
print ("\nEjercicio 6------>Escribe un programa que pida dos números enteros y calcule si la resta es positiva o negativa.\n")


##def positivo (x,y):
##    Eresta = True
##    operacion = x - y
##    if operacion <0:
##        Eresta = False
##    return Eresta
##x = int(input("Escribe el primer numero:"))
##y = int(input("Escribe el segundo numero:"))
##
##if positivo (x,y)==True:
##    print ("Es positivo")
##else:
##    print ("Es negativo")
##
def resta (x,y):
    return x-y

x = int(input("Escribe el primer numero:"))
y = int(input("Escribe el segundo numero:"))

if resta(x,y) <=0:
    print("Negativo")
else:
    print ("Positivo")


#EJERCICIO 7 -->Escribe un programa que pida dos números enteros e indique cuál es el mayor.
print ("\nEjercicio 7------>Escribe un programa que pida dos números enteros e indique cuál es el mayor.\n")

def mayor(x,y):
    if x > y:
        print (x)
    else:
        print (y)


x = int(input("Introduce un numero:"))
y = int(input("Introduce un numero:"))

mayor(x,y)


#EJERCICIO 8 -->Escribe un programa que pida dos números enteros e indique cuál es el menor.
print ("\nEjercicio 8------>Escribe un programa que pida dos números enteros e indique cuál es el menor.\n")

def menor(x,y):
    if x < y:
        print (x)
    else:
        print (y)

x = int(input("Introduce un numero:"))
y = int(input("Introduce un numero:"))

menor (x,y)


#EJERCICIO 9 -->Imprimir todos los números del 0 al 10.
print ("\nEjercicio 9------>Imprimir todos los números del 0 al 10.\n")

def numeros():
    for numeros in range(0,11):
        print (numeros)

numeros()


#EJERCICIO 10 -->Imprimir todos los números del 0 al 10, con un decimal.
print ("\nEjercicio 10------>Imprimir todos los números del 0 al 10, con un decimal.\n")

def unDecimal():
    lista = []
    numero = 0
    while numero < 10:
        lista.append(round(numero,2))
        numero += 0.1
    return lista
        

print(unDecimal())


#EJERCICIO 11 -->Imprimir todos los números del 0 al 10, con dos decimal.
print ("\nEjercicio 11------>Imprimir todos los números del 0 al 10, con dos decimal.\n")

def dosDecimales():
    lista = []
    numero = 0
    while numero < 10:
        lista.append(round(numero,3))
        numero += 0.01
    return lista

print (dosDecimales())




#EJERCICIO 12 -->Imprimir todos los números del 20 al 40, de dos en dos.    EXTRA [10,11,12]: Calcular la suma del resultado.
print ("\nEjercicio 12------>Imprimir todos los números del 20 al 40, de dos en dos.    EXTRA [10,11,12]: Calcular la suma del resultado.\n")

##def de2en2():
## for x in range(20,42,2):
##     print (x)                #MI METODO
##     
##de2en2()



def rangosalto (num,num2,salto):
    lista=[]
    for x in range(num,num2,salto):
        lista.append(x)
    return lista



num=int(input("Dame un valor para comenzar"))
num2=int(input("Dame un valor para finalizar"))
salto=int(input("Dame un salto"))
suma = num+num2
print (rangosalto(num,num2,salto))
print ("El resultado de la suma es")(suma)









        








    



    

    
    








    


    
