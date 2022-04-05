###EJERCICIO 1
##print ("EJERCICIO 1 \n")
##
##intr_seg = input("Introduce la hora en segundos:")
##segundos = int(intr_seg)
##
##horas = segundos // 3600
##sobra1 = segundos % 3600
##minutos = sobra1 // 60
##sobra2 = sobra1 % 60
##
##print ("Horas")
##print (horas)
##print ("Minutos")
##print (minutos)
##print ("Segundos")
##print (sobra2)





###EJERCICIO 2
##print ("EJERCICIO 2 \n")
##
##a = int(input("Introduce el valor de A:"))
##b = int(input("Introduce el valor de B:"))       
##c = int(input("Introduce el valor de C:"))
##
##x = -b / (2*a)
##y = a* (x**2) + b*x + c
##print (x)
##print (y)




###EJERCICIO 3
##print ("EJERCICIO 3 \n")
##
##hora1 = int(input("Introduce la primera hora"))
##hora2 = int(input("Introduce la segunda hora"))
##min1 = int(input("Introduce minuto 1"))
##min2 = int(input("Introduce minuto 2"))
##min1 = hora1*60+min1
##min2 = hora2*60+min2
##diferencia = abs(min2-min1)     
##print ("La diferencia de tiempo es de %d:%d" % (diferencia //60, diferencia%60))
##
##print (hora1 - hora2)





###EJERCICIO 4
##print ("EJERCICIO 4 \n")
##
##hora_1 = int(input ("Introduce una hora"))
##minuto_1 = int( input ("Introduce minutos"))
##hora_2 = int(input ("Introduce una hora"))
##minuto_2 = int( input ("Introduce minutos"))
##
##hora_total = (hora_1 - hora_2)
##minuto_total = (minuto_1 - minuto_2)
##
##print ( "%d Horas y  %d minutos" % (hora_total, minuto_total))




##EJERCICIO 5
##import random
##print ("EJERCICIO 5 \n")
##listaAleatoria = []
##for x in range (3):
##    numA = random.randrange(0,20)
##    listaAleatoria.append(numA)
##print (listaAleatoria)
##maximo = listaAleatoria[0]
##for x in listaAleatoria[1:]:
##    if x > maximo:
##        maximo = x
##print (maximo)



#EJERCICIO 6
##print ("Ejercicio 6 \n")
##
##a= int(input("Introduce a: "))
##b= int(input("Introduce b: "))
##b= int(input("Introduce c: "))
##if a==b==c:
##    print ("Son iguales los tres numeros")
##else if a==b or b==c or a==c:
##    print ("Son iguales los dos")
##else:
##    print ("No son iguales")

##
###EJERCICIO 7
##print ("Ejercicio 7 \n")
##
##x = int(input("Introduce x:"))
##lista = []
##for i in range (1,x,2):
##    lista.append(i)
##print (lista)

#EJERCICIO 8
print ("Ejercicio 8 \n")
texto = input("Introduce texto:")
mayusculas = 0
minusculas = 0
otro = 0

for letra in texto:
    if ord(letra)>= 64 and ord (letra)<=90:
        mayusculas += 1
    elif ord (letra) in [97,122]:
        minusculas
    else:
        otro += 1
print (mayusculas, minusculas, otro
       )
        



















    

    
