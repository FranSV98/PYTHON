#lista = [" "]
#len (lista)
#min (lista)
#max (lista)
#sum (lista)
#dato in lista
#lista.index (valor)
#lista.count (valor)
#print (any (lista))
#print (all(lista)


"""
def sumarDosListas ( lista1, lista2):
    listaSuma = []
    for elemento in lista1:
        listaSuma.append(elemento)
    for elemento in lista2 : 
        listaSuma.append(elemento)
    return listaSuma




lista1= list("321654984213684693843")
lista2 = list ("64131346155161165984")
listaSuma = sumarDosListas (lista1, lista2)

print (listaSuma)"""

import random
def listaNumerosAleatorio(tama,menor,mayor):
    listaAleatoria = []
    for elemento in range(tama):
        n = random.randrange(menor,mayor)
        listaAleatoria.append(n)
    return listaAleatoria
def listaSumaElementosDeDosListas(lista1,lista2):
    listaSuma = []
    posicion = 0
    for elemento in lista1:
        posicion = lista1.index(elemento)
        suma = lista1[posicion]+lista2[posicion]
        listaSuma.append(suma)
        posicion += 1
    return listaSuma
lista1 = listaNumerosAleatorio(20,0,20)
lista2 = listaNumerosAleatorio(20,0,20)
print (lista1)
print (lista2)
listaResultado = listaSumaElementosDeDosListas(lista1,lista2)
print (listaResultado)
