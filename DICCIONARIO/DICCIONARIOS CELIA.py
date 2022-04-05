##list () o lista[]       Ordenada, Modificable, Datos duplicados, Indice.
##tuple () o tupla()      Ordenada, No modificable, Datos duplicados, Indice.
##set () o seta {}        No ordenada, No modifica datos, pero crea y elilmina, Sin datos duplicados, Sin indice.
##dict () o deccionario   Ordenados, Modificable, Datos duplicados, Sin indice, pero con Clave.

def crearDiccionarioListaValor(listaClaves,valorInicial):
    for elemento in listaClaves:
        dicc.update({elemento:valorInicial})
    return dicc
    



"""
lista = ["rojo", "naranja", "amarillo", "verde", "azul", "morado"]
tupla = ("rojo", "naranja", "amarillo", "verde", "azul", "morado")
seta = {"rojo", "naranja", "amarillo", "verde", "azul", "morado"}
diccionario = {
    "rojo":3,
    "naranja":1,
    "amarillo":1,
    "verde":2,
    "azul":5,
    "morado":0,
    "LM":[6, 7.2]
}

print (seta)
print (diccionario)
print (len(seta))
print (len (diccionario))

print (diccionario["amarillo"])
print (diccionario.get ("amarillo"))
print ("verde" in seta)
print ("rosa" in seta)
print (diccionario.keys())
print (diccionario.values())
print (diccionario.items())

print (diccionario["verde"])
print (diccionario.get("verde"))
#print (diccionario[3]) NO FUNCIONA, EL INDICE ES LA CLAVE, NO LA POSICIÓN

print (diccionario["LM"])
print (diccionario["LM"][0])


primerElementoDeLaListaNotasLM = diccionario ["LM"][0]
#Esto se puede hacer en dos pasos:
#ver el valor almacenado en la clave "LM"
valor = diccionario ["LM"]
#accedemos al primer elemento de esa lista
primerElemento = valor [0]


#Para modificar un valor del diccionario:
diccionario ["azul"] = 4
print (diccionario)
#O con la función
diccionario.update({"azul":7})
print (diccionario)

#Para añadir un item:
diccionario ["Negro"] = 2
print (diccionario)
#O con la función
diccionario.update ({"blanco":3})



###________RESPECTO AL SET__________###
print ("_______________CON RESPECTO AL SET")

seta.add ("negro")
print (seta)

seto = {"blanco", "marron"}
seta.update (seto)
print (seta)

seti = {"rosa", "gris"}
#seta.add (seti) NO FUNCIONA
#seta.union (seti) ASÍ NO!!!
sete = seta.union (seti)
print (seta)
#.update agrega todos los elementos pero sin duplicidades.
print (".....INTERSECCIÓN........")
setZ = {"rojo", "naranja", "amarillo"}
setY = {"amarillo", "verde", "azul"}
print (setZ.intersection (setY))

print (".......DIFERENCIA......")
print (setZ.difference(setY))

print ("........DIFERENCIA SIMÉTRICA.........")
print (setZ.symmetric_difference (setY))


#seta = seta+seto    NO PUEDES + SET

seta.remove ("marron")
print (seta)
#seta.remove ("marron")     NO PUEDES ELIMINAR ALGO QUE NO ESTÁ
seta.discard ("negro")
print (seta)
seta.discard ("negro")    # SÍ PUEDES DESCARTAR COSAS QUE NO ESTEN, LO ELIMINARÁ SI EXISTE
print (seta)

seta.clear() #  ELIMINA TODOS LOS ITEMS DE UNA SOLA VEZ
print ("VAMOS")
print (seta)

#del seta       ELIMINA EL CONTENIDO DE LA VARIABLE DEJÁNDOLA INDEFINIDA




###_________RESPECTO AL DICCIONARIO___________###
print ("____________________RESPECTO AL DICCIONARIO")
diccionario.pop ("azul")
print (diccionario)
diccionario.popitem() # ELIMINA LO ÚLTIMO QUE HEMOS INTRODUCIDO
print (diccionario)

#diccionario.clear   #ELIMINA LOS ITEMS
#del diccionario     #DEJA LA VARIABLE SIN DEFINIR



###__________BUCLES__________###


print ("______________LISTA")
for elemento in lista:
    print (elemento)
    
print ("______________TUPLA")
for elemento in tupla:
    print (elemento)

print ("______________SET")
for elemento in seta:
    print (elemento)

print ("______________DICT")
for elemento in diccionario:
    print (elemento)

print ("______________DICCIONARIO/CLAVES")
for clave in diccionario:
    print (clave)

print ("______________DICCIONARIO/CLAVES2")
for clave in diccionario.keys():
    print (clave)

print ("______________DICCIONARIO/VALORES")
for clave in diccionario:
    print (diccionario[clave])

print ("______________DICCIONARIO/VALORES2")
for elemento in diccionario.values():
    print (elemento)

print ("______________DICCIONARIO/CLAVES+VALORES")
for clave in diccionario:
    print (clave, diccionario[clave])

print ("______________DICCIONARIO/CLAVES+VALORES2")
for clave, valor in diccionario.items():
    print (clave, valor)"""


diccCamisetas = {
    "Celia":    "roja",
    "Marco":    "gis",
    "Fer":      "blanca",
    "Javi":     "azul",
    "Vicky":    "negra",
    "Carlos":   "negra",
    "Rafa":     "azul",
    "Charlie":  "negra",
}

setCamisetas = set()
setCamisetas.update(diccCamisetas.values())
print (len(setCamisetas))

#¿Cuantas camisetas tenemos de cada color?
#Creamos un diccionario que tenga como clave los colores y como valor inicial de todas las claves "0"

nuevoDicc = crearDiccionarioListaValor(setCamisetas,0)
print (neuvoDicc)

for elemento in diccCamisetas.values():
    nuevoDicc[elemento] +=1

print (nuevoDicc)

for clave in nuevoDicc:
    if nuevoDicc[clave] >1:
        print ("La camiseta %s se repite %d veces"%(clave))








