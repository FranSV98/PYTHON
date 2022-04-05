#EJERCICIO 1 (SOLICITAR UN NUMERO Y DEVOLVER UNA LISTA CON SUS DIVISORES)
print ("Introduzca el numero")
numero = int(input())
cont = 0
print ("Los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
             print (divisor,"Es divisor")
             cont += 1
print ("El numero", numero,"tiene",cont,"divisores")


#EJERCICIO 2 (SOLICITAR NUMEROS, DEVOLVER SI SON PARES O IMPARES, EL PROGRAMA TERMINA AL ESCRIBIR SALIR)
numero = ""
fin = "salir"
while numero !=fin:
    numero = input("Escribe una numero:")