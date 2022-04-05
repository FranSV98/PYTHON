def sumador_iteracion(inicio, dias):
    recogida = inicio
    total = inicio
    for i in range(1, dias):
        recogida *= 2
        total += recogida
    return total

def sumaDobleCadaIteracion (inicio, numIteraciones) :
    cantidadIteracion = inicio
    total = inicio
    for numero in range ( 1, numIteraciones):
        cantidadIteracion *= 2
        total += cantidadIteracion
        print (cantidadIteracion, total)
    return total

def dividirNumeroEntreOtro (num1, num2):
    return num1//num2

def crearSetConLista(lista):
    nuevoSet = set()
    nuevoSet.update(lista)
    return nuevoSet

def crearDiccConLista(lista,valor):
    diccColoresNum = dict()
    for elemento in lista:
        nuevoDicc.update({color:valor})
    return nuvoDicc

def diccContarOcurrenciasEnLista(lista):
    nuevoDicc = crearDiccConLista(lista,0)
    for elemento in lista:
        nuevoDicc[elemento] += 1
    return nuevoDicc

def diccCategorizar(diccionario):
    



#--------------------------------------------
print ("Ejercicio 2")
primerDia = 1
numeroDias = 14
manzanasUltimoDia = sumaDobleCadaIteracion (primerDia, numeroDias)
print ( manzanasUltimoDia)


###EJERCICIO 3-----------------------------------------

print ("Ejercicio 3")
manzanasPorTarta = 4
numeroTartas = dividirNumeroEntreOtro (manzanasUltimoDia, manzanasPorTarta)
print ("Con %d manzanas puedo hacer %d tartas" % (manzanasUltimoDia,numeroTartas))

###EJERCICIO 4-----------------------------------------
print ("Ejercicio 4")
diccManzanas = {
    "Fuji" : "roja",
    "Gala" : "amarilla",
    "Golden" : "amarilla",
    "Red Delicius": "roja",
    "Pink Lady" : "roja",
    "Granny Smith" : "verde"
}
print (diccManzanas)

###EJERCICIO 5-----------------------------------------
print ("Ejercicio 5")
setColores = crearSetConLista(diccManzanas.values())
numColores = len(setColores)
print ("Hay %d colores de manzanas" % numColores)

###EJERCICIO 6-----------------------------------------
print ("Ejercicio 6")
diccColoresNum = diccContarOcurrenciasEnLista(diccManzanas.values())
print (diccColoresNum)

###EJERCICIO 7-----------------------------------------
print ("Ejercicio 7")
diccColoresTipo = diccCategorizado(diccManzanas)







