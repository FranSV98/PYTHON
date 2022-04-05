"""
ESTE EXAMEN ES EL ULTIMO Y ESPERO SACAR MINIMO UN 5 xD
@date 17.12.21
"""
import random
##FUNCIONES

##
##fn def meGustaNavidad(palabra)
#@brief Devuelve una frase u otra, dependiendo de la contestacion NAVIDAD/navidad
#@param palabra String
#@return String
def meGustaNavidad(palabra):
    if palabra == "NAVIDAD":
        iLike = "CONTINUEMOS"
    elif palabra == "navidad":
        iLike = "continuemos"
    else:
        iLike = "Asumire que SI!!"
    return iLike

##
##fn def quieroCaramelos(palabra)
#@brief Devuelve una frase u otra, dependiendo de la contestacion SI/NO
#@param palabra String
#@return String
def quieroCaramelos(palabra):
    if palabra == "SI":
       caramelos = (random.randint(10,100))
    elif palabra == "NO":
        caramelos = "MAS PARA MI JEJE!"
    else:
        caramelos = "PUES NO TE DOY!"
    return caramelos

##
##fn reyesMagos(palabra)
#@brief Devuelve una frase u otra, dependiendo de la contestacion SI/NO
#@warning ESTA FUNCION TE QUITA LA ILUSION
#@param palabra String
#@return String
def reyesMagos(palabra):
    if palabra == "SI":
        responde = "SIGUE CON TU ILUSION INSENSATO/A"
    elif palabra == "NO":
        responde = "PUES SON LOS PADRES!!"
    else:
        responde = "EL DIA QUE SEPAS LA VERDAD NO QUEDRAS VIVIR!!"
    return responde

    

##EJERCICIO 1
print("EJERCICIO 1_____>")
regalo = input("Queridos Reyes Magos, ¡este año me he portado muy bien!Por eso me gustaría que me trajérais:")
nombre = input("ATTM:")

##EJERCICIO 2
print("EJERCICIO 2_____>")
pregunta = input("¿Te gusta la Navidad?: ")
contestacion = meGustaNavidad(pregunta)
print (contestacion)

##EJERCICIO 3
print("EJERCICIO 3_____>")
pregunta = input("¿A ti te gustan los caramelos?: ")
contestacion = quieroCaramelos(pregunta)
print (contestacion)

##EJERCICIO 4
print("EJERCICIO 4_____>")

armas = ["Paraguas", "BateDeBeisbol", "BastonDeCaramelo", "GorritoGracioso", "AmorCursi", "SeñoraRecogeCaramelos"]
seleccionArma = input("Que arma te gustari utilizar? Elige del 1 al 6:")


##EJERCICIO 5
print("EJERCICIO 5_____>")

dicNombreEdad = {
    "Sofia":10,
    "Edu":8,
    "Lucas":7,
    "Alicia":12,
    "Leo":6,
    "Erika":5
}
sumaEdad = int(10+8+7+12+6+5)
cuenta = (52-sumaEdad)
print ("Sobrarian %d caramelos"% (cuenta))
##EJERCICIO 6
print("EJERCICIO 6_____>")

parejas = ["Alicia","Erika"], ["Sofia","Leo"],["Edu","Lucas"]
cuentaListaParejas = int(52/3)
print ("Cada pareja se llevaria %d caraemlos"% (cuentaListaParejas))

##EJERCICIO 7
print("EJERCICIO 7_____>")
print ("Tenemos los suficientes caramelos porque todavia quedan %d"% (cuenta))
print ("Cada pareja se llevaria %d caramelos"% (cuentaListaParejas))

##EJERCICIO 8
print("EJERCICIO 8_____>")

##EJERCICIO 9
print("EJERCICIO 9_____>")

##EJERCICIO 10
print("EJERCICIO 10_____>")

##EJERCICIO 11
print("EJERCICIO 11_____>")
reyes = input("Sabes quien son los REYES MAGOS?:")
contestacion = reyesMagos(reyes)
print (contestacion)









