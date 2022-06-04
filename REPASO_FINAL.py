
import random

nombre = "Pablo de Cara Jiménez"
print (nombre)

# 18

##palabra = input ("Introduce una palabra: ")
##palabra = palabra.lower()
##primera = (palabra[0]).upper()
##salida = primera+palabra[1:]
##print (salida)

# 20

##def invierteString(palabra):
##    salida = ""
##    cont = 1
##    for l in palabra:
##        salida = salida+palabra[-cont]
##        cont += 1
##    return salida
##
##def esPalindromo(palabra):
##    palabra = palabra.upper()
##    es = False
##    inver = invierteString(palabra)
##    if inver == palabra:
##        es = True
##    return es
##
##palabra = input ("Introduce una palabra: ")
##print (invierteString(palabra))
##
##print (esPalindromo(palabra))

# 21 / 25

def generaListaAleatoria(cantidad, rango):
    lista = []
    for x in range(cantidad):
        lista.append (random.randrange(0,rango))
    return lista

def soloPares(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] %2 == 0:
            pares.append (lista[i])
    return pares

def soloImpares(lista):
    impares = []
    for i in range(len(lista)):
        if lista[i] %2 != 0:
            impares.append (lista[i])
    return impares


miLista = generaListaAleatoria(10,100)
misPares = soloPares(miLista)
misImpares = soloImpares(miLista)
print ("MI LISTA: ", end="")
print (miLista)
print ("MIS PARES: ", end="")
print (misPares)
print ("MIS IMPARES: ", end="")
print (misImpares)

# 31 (mejor planteamiento: no hay que meter -1 para terminar, pide cada asignatura y termina)

def pideNotas(asignaturas):
    notas = []
    for i in range(len(asignaturas)):
        laNota = float(input("Introduce la nota de "+asignaturas[i]+": "))
        notas.append(laNota)
    return notas

def calculaMedia(notas):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i]
    return suma/len(notas)

todas = input ("Escribe el nombre de las asignaturas separadas por un espacio: ")
asignaturas = todas.split()
notas = pideNotas(asignaturas)
media = calculaMedia(notas)
print ("MEDIA:", end =" ")
print (media)


# 32

def calculaMedia(notas):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i]
    return suma/len(notas)

def pideAsigYNotas(asig, notas):
    entrada = ""
    while (entrada != "-1"):
        entrada = input("Introduce la asig y la nota separados por espacio: ")
        if entrada != "-1":
            datos = entrada.split()
            asig.append(datos[0])
            notas.append(int(datos[1]))
    
asignaturas = []
notas = []
pideAsigYNotas(asignaturas, notas)

print (asignaturas)
print (notas)

print ("MEDIA:", end =" ")
print (calculaMedia(notas))

# 38

def esNumero(string):
    numero = True
    if string == "":
        numero = False
    for i in string:
        if i not in "1234567890":
            numero = False
    return numero
  
def esLetra(string):
    numero = True
    if string == "":
        numero = False
    for i in string:
        if i not in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
            numero = False
    return numero

def esDNI(dni):
    resp = True
    if len(dni) != 9:
        resp = False
    elif esNumero(dni[0:8])== False or esLetra(dni[8])== False:
        resp = False
    return resp

def compruebaLetraDNI(dni):
    letraOK = True
    letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    numeros = dni[0:8]
    suma = 0
    for i in range(len(numeros)):
        suma += int(numeros[i])
    pos = int(numeros) %23
    if letras[pos] != dni[8]:
        letraOK = False
    return letraOK

def compruebaDNI(dni):
    salida = ""
    if esDNI(dni):
        if compruebaLetraDNI(dni):
            salida = "DNI CORRECTO."
        else:
            salida = "LA LETRA NO CORRESPONDE."
    else:
        salida = "EL FORMATO NO ES CORRECTO."
    return salida


miDNI = ""
ok = ""
while ok != "DNI CORRECTO." and miDNI != "salir":
    miDNI = input("INTRODUCE DNI: ")
    if miDNI != "salir":
        ok = (compruebaDNI(miDNI))
        print (ok)
    else:
        print ("Adios.")

        

## PARA ORDENAR DE MAYOR A MENOR
def ordenaListaMayorMenor(lista):
    ordenadaMm = []
    for x in range (len(lista)):
        mayor = lista[0]
        for y in lista:
            if y >= mayor:  # <= PARA ORDENAR DE MENOR A MAYOR
                mayor = y
        ordenadaMm.append (mayor)
        lista.remove (mayor)
        
    return orden
























