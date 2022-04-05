"""
Examen Diccionarios
Documentacion de examen hasta diccionarios .
Realizado el 10.12.2021
Examen Buleanos
@author Francisco Soto Vera
@version 0.1
@date 10/12/2021
@warning Este codigo esta incompleto
@Copyright Este codigo no se puede copiar
"""
import random
#FUNCIONES
#@fn nombresLargoOcorto(nombre)
#@brief sirve para indicar si te gustan o no los perros
#@param nombre
def nombresLargoOcorto(nombre):
    for letras in nombre:
        if nombre >6:
            print(corto)
        else:
            print(largo)
            
#@fn listaAleatorios
#@brief Genera una lista de numeros aleatorios
#@param n
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(2, 90)
      return lista

    
#@fn mediaPeso(peso)
#@brief Calcula la media de peso de los perros
#@param peso
def mediaPeso(peso):
    media = sum(peso)/len(peso)
    return media
    
        

#CODIGO

##EJERCICIO 1
print ("EJERCICIO 1-->")
print ("Francisco Soto Vera\n")


##EJERCICIO 2
print ("EJERCICIO 2-->")

perros = input("Te gustan los perros?:")
si = ("A mi tambien me gustan\n")
no = ("Mala bomba te caiga\n")

if perros:
    print (si)
else:
    print (no)
    

##EJERCICIO 3
print ("EJERCICIO 3-->")

nombre = input("Cual es el nombre de tu perro?:")

largo = input("El nombres es demasiado largo\n")
corto = input("I like this name\n")


##EJERCICIO 4
print ("EJERCICIO 4-->")

nombre = ("Gran Danés","Mastín","Bretón ","Puli ","Boxer ","Fox Terrie","Galgo ","SanBernardo ","Labrador ","Perro salchicha","Dálmata")
peso = (67,82,16,12,28,8,30,65,29,10,25)

##EJERCICIO 5
print ("EJERCICIO 5-->")
print("Ingrese cuantos numeros aleatorios desea obtener:")
n=int(input())

aleatorios=listaAleatorios(n)
print(aleatorios)

##EJERCICIO 6
print ("EJERCICIO 6-->\n")

##EJERCICIO 7
print ("EJERCICIO 7-->")
print (mediaPeso(peso))













