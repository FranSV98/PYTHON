#Hola mundo
print ("Hola mundo ---------->")
print ("Hola mundo\n")



#Variables y tipos
print ("\nVariables y tipos---------->") 

mystring = "Hello"  
myfloat = 10
myint = 20
print ("Este es el nombre %s, este el numero %d, y este el entero %d.\n" % (mystring, myfloat,myint))




#Listas
print ("\nListas---------->")
numeros = [1,2,3]
cadena = ["hola" , "mundo"]
print (numeros)
print (cadena)

numeros.append("hola\n")
for elemento in numeros:
    print (elemento)

cadena.append(4)
for elemento in cadena:
    print (elemento)




#Operadores basicos
print ("\n Operadores Basicos---------> ")

x = object()
y = object()

# Cambia este código
x_lista = [x]*10
y_lista = [y]*10
gran_lista = x_lista + y_lista

print ("x_lista contiene %d objetos" % len(x_lista))
print ("y_lista contiene %d objetos" % len(y_lista))
print ("gran_lista contiene %d objetos" % len(gran_lista))

# Código de prueba
if x_lista.count(x) == 10 and y_lista.count(y) == 10:
    print ("Casi llegamos...")
if gran_lista.count(x) == 10 and gran_lista.count(y) == 10:
    print ("Genial!")

    





#Formatos de texto
print ("\n Formatos de texto--------->")

datos = ("Juan", "Perez", 53.44)
format_string = "Hola %s %s. Tu balance es de %f $."

print(format_string % datos)







#Operaciones Basecias con texto
print ("\n \n Operaciones basicas con texto--------->")

s = "Hola ahi! Que debe ser esta cadena?"

# Longitud debe ser 35
print ("Longitud de s = %d" % len (s))

# Primer evento de "a" deberá estar en el lugar 3
print ("Primer evento de la letra a = %d" % s.index("a"))

# El número de a's deberá ser 5
print ("a ocurre %d veces" % s.count("a"))

# Slicing the string into bits
print ("Los primeros cinco caracteres son '%s'" % s[:5]) # Start to 5
print ("Los siguientes cinco caracteres son '%s'" % s[5:10]) # 5 to 10
print ("La decimotercera personaje es '%s'" % s[12]) # Just number 12

print ("Los ultimos cinco caracteres son '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print ("Cadena en mayusculas: %s" % s.upper())

# Convert everything to lowercase
print ("Cadena en minusculas: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print ("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print ("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print ("Split the words of the string: %s" % s.split(" "))

#Condicionales
print ("\n Condicionales--------->")

# Cambia este codigo
number = 20
second_number = 0
first_array = [1,1,2]
second_array = [1,2]

# No cambies este código
if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")







#Bucle
print ("\n Bucle---------->")

numeros = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

      
for pares in numeros:
    if(pares<412):
        if(pares%2==0):
            print(pares)
       

   
