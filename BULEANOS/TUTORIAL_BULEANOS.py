"""@pakage Mi Primer Proyecto
Aqui hablamos de nuestro proyecto
Añadims un moneton de detalles
Como po ejemplo el autor
"""

##    """
##    @fn def numeroEsMultiploOtro(numero,otroNumero)
##    @brief Comprueba si un numero es multiplo de otro.
##    @pre El parametros otro numero no puede ser igual a 0.
##    @post
##    @param numero Numero.
##    @return Devuelve un buleano.
##    """

def esDos(numero):
    return numero==2

def esPositivo (numero):
    return numero >=0

def esNegativo (numero):
    return numero <=0

def numeroEsMultiploOtro(numero, otroNumero):
    return numero%otroNumero>= 0

def numeroEsMayorQueOtro(numero,otroNumero):
    return numero>otroNumero

def numeroEsMenorQueOtro(numero,otroNumero):
    return numero<otroNumero

def numeroEsIgualQueOtro(numero,otroNumero):
    return numero==otroNumero

def numeroEsPar(numero):
    return numero %2==0

def numeroEsMultiploDeTres(numero):
    return numero %3==0

def numeroEsMultiploDeOtroNumero(numero,otroNumero):
    return numero%otroNumero

def numeroEsDivisorDeOtro(numero,otroNumero):
    return otroNumero%numero==0

def numeroTerminaEnSiete(numero):
    return numero%10==7

def numeroEsIgualQueOtro(numero,otroNumero):
    return numero==otroNumero

def numeroEsPrimo(numero):
    EsPrimo = True
    iterador = 2
    while EsPrimo and iterador<numero:
        if numero%iterador == 0:
            EsPrimo = False
        iterador+=1
    return EsPrimo

def letraEsMayuscula(letra):
    return letra>="A" and letra<="Z"

def letraEsMinuscula(letra):
    return letra>="a" and letra<="z"

def caracterEsLetra(letra):
    mayuscula = letraEsMayuscula(letra)
    minuscula = letraEsMinuscula(letra)
    return mayuscula or minuscula

def caracterEsNumero(numero):
    return numero>="0" and numero<="9"
    
def letraEsVocal(letra):
    letra = letra.lower()
    return letra in "aeiou"

def letraEsIgualaOtra(letra1, letra2):
    return letra1==letra2

def letraEsConsonante(letra):
    return caracterEsLetra(letra) and not letraEsVocal(letra)

def listaNombreConsonantes(listaNombres, letra):
    nuevaListaPalabras = []
    for palabra in listaNombres:
        if letraEsIgualaOtra(letra,palabra[0]):
            nuevaListaPalabras.append(palabra)
    return nuevaListaPalabras
        
#--------------------------------------------------------

listaNombres = ["Alvaro", "Fernando", "Marco", "Joel","IsmaelBa","Pablo","Manu","Mikel","Javi","Emilio","Rafa","Charlie","Juanmi","Vicky","PacoJavi","Carlos","Soto"]

print ("esDos------>")
resultado = esDos(5)
print (resultado)

print ("\nesPositivo------>")
resultado = esPositivo(-5)
print(resultado)

print ("\nesPositivo------>")
resultado = esPositivo(5)
print(resultado)

print ("\nnumeroEsMayorQueOtro------>")
resultado = numeroEsMayorQueOtro(5, 10)
print(resultado)

print ("\nnumeroEsMenorQueOtro------>")
resultado = numeroEsMenorQueOtro(5, 2)
print(resultado)

print ("\nnumeroEsIgualQueOtro------>")
resultado = numeroEsIgualQueOtro(10, 10)
print (resultado)

print ("\nnumeroEsPar------>")
resultado = numeroEsPar(23)
print (resultado)

print ("\nnumeroEsMultiploDeTres------>")
resultado = numeroEsMultiploDeTres(23)
print (resultado)

print ("\nnumeroEsDivisorDeOtro------>")
resultado = numeroEsDivisorDeOtro(12, 6)
print (resultado)

print ("\nnumeroTerminaEnSiete------>")
resultado = numeroTerminaEnSiete(37)
print (resultado)

print ("\nnumeroEsIgualQueOtro------>")
resultado = numeroEsIgualQueOtro(34, 34)
print (resultado)

print ("\nnumeroEsPrimo------>")
resultado = numeroEsPrimo(2)
print (resultado)

print ("\nletraEsMayuscula------>")
resultado = letraEsMayuscula("H")
print (resultado)

print ("\nletraEsMinuscula------>")
resultado = letraEsMinuscula("H")
print (resultado)

print ("\ncaracterEsLetra------>")
resultado = caracterEsLetra("Hola")
print (resultado)

print ("\ncaracterEsNumero")
resulado = caracterEsNumero("5")
print (resultado)


print ("\nletraEsVocal------>")
resultado = letraEsVocal("i")
print (resultado)

print ("\nletraEsConsonante------>")
resultado = letraEsConsonante("j")
print (resultado)

print ("\nlistaNombreConsonantes------>")
letra = input("Introduzca una letra en MAYUSUCULA:")
nuevaListaNombres = listaNombreConsonantes(listaNombres,letra)
print(nuevaListaNombres)

