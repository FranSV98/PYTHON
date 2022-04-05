def comparaNotas (nota1, nota2):
    masDeDos = False                #Calcula la diferencia entre don notas.
    difer = nota2 - nota1
    if difer > 2:
        masDeDos = True
    return masDeDos

def asegurar ():            #Pregunta si estás seguro
    SiONo = input ("¿Estás seguro/a de haber introducido las notas correctamente? ")
    SiONo = SiONo.upper()
    return SiONo

def pideNotas():
    dife = True             #Solicita las dos notas y si la dif es > 2 pregunta
    while dife == True:
        notaA = int (input ("Introduce la nota antigua: "))
        notaN = int (input ("Introduce la nota nueva: "))
        dife = comparaNotas (notaA, notaN)
        if dife:
            comp = asegurar()
            if comp == "SI":
                dife = False

def pideEdad ():                        #Solicita la edad.
    edad = int (input( "Introduce tu edad: "))
    return edad

def pideApellido ():                    #Solicita el apellido
    apellido = (input( "Introduce tu apellido: "))
    return apellido

def comparaEdad (edad):                 #Comprueba si eres mayor de edad
    return edad < 18

def clasifica (apellido):               #Clasifica en filas según apellido
    apellido = apellido.upper()
    clase = 0
    if apellido >= "A" and apellido <= "G":
        clase = "Estás en la Fila 1"
    elif apellido >= "H" and apellido <= "N":
        clase = "Estás en la Fila 2"
    else:
        clase = "Estás en la Fila 3"
    return clase

#....................................................................

nombre = "Pablo de Cara Jiménez"
print (nombre)

pideNotas()

print ("OK")

edad = pideEdad()
apellido = pideApellido()

if comparaEdad (edad):
    print ("Estás en la Fila Especial.")
else:
    clase = clasifica (apellido)
    print (clase)
    
salir = input ("Enter para salir. ") 		# Esto es solo para que no salga automáticamente
