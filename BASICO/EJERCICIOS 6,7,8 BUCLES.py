###Ejercicio 6

numero = int(input("Introduce un numero entero para crear el triangulo rectangulo:"))
for a in range(numero):
    for b in range(a+1):
        print("*", end="")
    print("")




#Ejercicio 7
    
for t in range(1, 11):
    for b in range(1, 11):
        print(t*b, end="\t")
    print("")
        



#Ejercicio 8

num = int(input("Introduce un numero entero: "))
for x in range(1, num+1, 2):
    for a in range(x, 0, -2):
        print(a, end=" ")
    

