"""
REPASO
"""
#--------------------------------------------------------#
#                    FUNCIONES                           #
#--------------------------------------------------------#
##
#@fn presentacion()
#@brief Recibiendo un nombre, una edad y un videojuego, va a p
#@param string n
#@param int ed
#@param sting jue
def imprimePresentacion(nom,ed,jue):
    print ("Hola me llamo %s y tengo %d años y mi juego favorito es el %s" % (nom, ed, jue))
"""
def solcitarNombre():
    nom = input("¿Como te llamas? ")
    return nom

def solicitaJuego():
    juego = input("¿Cual es tu juego favorito? ")
    return juego"""

def solicitar(frase):
    return (input(frase))

def solicitarInt(frase):
    return int(input(frase))

def funcionPresentacion():
    nombre = solicitar(preguntaN)
    while len(nombre)>0:
        edad = solicitarInt(preguntaE)
        juego = solicitar(preguntaJ)

        imprimePresentacion(nombre,edad,juego)

#--------------------------------------------------------#
#                      VARIABLES                         #
#--------------------------------------------------------#
preguntaN = "¿Como te llamas? "
preguntaE = "¿Cuantos años tienes? "
preguntaJ = "¿Cual es tu juego FAV? "
preguntaContinuar = "¿Quieres seguir? "
#--------------------------------------------------------#
#                      CODIGO                            #
#--------------------------------------------------------#
##while True:
##    palabra = solicitar ("Introduce una palabra:")
##    letra = solicitar ("Introduce una letra:")
##    i = 0
##    tieneLetra = False
##    while i<len(palabra):
##        letraPalabra = palabra[i]
##        if letra == letraPalabra:
##            tieneLetra = True
##        i += 1
##    print ("La palabra %s tiene la letra %s" % (palabra, i))
##    if tieneLetra:
##        print ("Esta palabra contiene la %s" % letra)

while True:
    frase = solicitar ("Introduce dos palabras:")
    i = 0
    listaPalabras = []
    nuevaPalabra = ""
    espacioEncontrado = False
    while i <len(frase):
        letra = frase[i]
        if frase[i] == " ":
            listaPalabras.append(nuevaPalabra)
            nuevaPalabra = ""
        else: 
            nuevaPalabra += letra
        i += 1
    listaPalabras.append(nuevaPalabra)
    print (listaPalabras)

    while i<len(nuevaPalabra):
        letra = letra[i]
        if frase[i] == "a":
            listaNuevasPalabras.append(nuevaPalabra)
            nuevaPalabra = ""
        else: 
            nuevaPalabra += letra
    
        
        
        





























"""
    vocales = "aeiou"
    letra = solicitar("Introduce una letra")
    esVocal = False
    indice = 0
    while indice < len(vocales) and not esVocal:
        if letra == vocales[indice]:
            esVocal = True
        print (vocales[indice])
        indice += 1
"""
"""
    for vocal in vocales:
        print ("La letra es", letra)
        print ("La vocal es", vocal)
        if letra == vocal:
            esVocal = True
            """






    
    
