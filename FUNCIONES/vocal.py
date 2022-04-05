# lista1 = list("PASTILLAS")
# string = list("ASD")

# print("\nAñadir otra lista: ")
# lista1.extend(string)
# print(lista1)
# print("\nLista ordenada de menor a mayor o alfabeticamente")
# lista1.sort()
# print(lista1)
# print("\nGirar la lista: ")
# lista1.reverse()
# print(lista1)

def list_to_string(lista):
    final = ""
    lista.reverse()
    for i in lista:
        final += i
    return final

def contar_vocales(cadena, letra):
    contador = 0
    cadena.lower()
    letra.lower()
    for i in cadena:
        if i == letra:
            contador += 1
    return contador

def eliminar_letra(cadena, letra):
    lista = list(cadena)
    lista.reverse()
    lista.remove(letra)
    return lista

# def eliminar_letra_fast(lista, letra):
#     indice = 0
#     posicion = "NO"
#     for i in lista:
#         if i == letra:
#             posicion = indice
#         indice += 1
#     lista.pop(posicion)

cadena = input("\nEscribe una frase: ")
vocal = input("\nEscribe una vocal: ")

contar_vocal = contar_vocales(cadena, vocal)

print('\nHay %d %s en "%s"' %(contar_vocal, vocal, cadena))

letra = input("\n¿Qué letra quieres eliminar? ")

eliminar_l = eliminar_letra(cadena, letra)

eliminar_final = list_to_string(eliminar_l)

print(eliminar_final)