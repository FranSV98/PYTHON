#Divisores de 5

lista = []
for n in range (1,100):
    if n %5==0:
        lista.append(n)
print (lista)

#Ejercicio dados
import random

while True:
    resultado = random.randint(1,6)
    print("El dado giro y obtuvo: "), resultado
    input("Presiona cualquier tecla para lanzar nuevamente.")
    

