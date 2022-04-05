##Diseñar un programa que lea una cadena y un numero entero al que llamamos x
##Tiene que devolver cuantas palabras tienen la longitud x



#EJERCICIO 1
print('Programa que lea una cadena y un entero y nos diga cuántas palabras tienen la misma longitud que el entero')
 
cadena = ('Los últimos informes de Sanidad alertan del incremento de transmisión del virus ')
k = int(input('Dime un número entero: '))
x = cadena.split()
palabras_k = []
for palabra in x:
  if (len(palabra) == k):
    palabras_k.append(palabra)
 
if (len(palabras_k) > 0):
  mas = 'as' if len(palabras_k) > 1 else 'a'
  print('Hay %s palabr%s con la longitud de %s caracteres:' % (len(palabras_k), mas, k))
  for palabra in palabras_k:
    print('Palabra: %s' % palabra)
else:
    print('No hay ninguna palabra con la longitud de %s caracteres' % k)


#EJERCICIO 2

#EJERCICIO 3
b = input("Introduce un numero binario:")
posicion = 0
resultado = 0
for num in b:
  resto = int (b) %10
  b = int(b) / 10
  resultado = resultado + resto * 2** posicion
  posicion += 1
if resto <2:
  print (resultado)
else:
  print ("Ese numeros no es binario")







