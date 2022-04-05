#FUNCIONES
def diferenciaNumeros(num1,num2):
    return num1-num2

def numeroMayorOtro(num1,num2):
    return num1>num2

def palabraIgualOtra(pal1,pal2):
    return pal1==pal2

def letraEntreLetras(letra,letrasIni,letraFin):
    return letra>=letraIni and letra<=letraFin

def asignarFila(edad, apellido):
    if numeroMayorOtro(edad,18):
        if letraEntreLetras(apellido[0],"A", "G"):
            fila = "FILA 1"
        elif letraEntreLetras(apellido[0], "H", "N"):
            fila = "FILA 2"
        else:
            fila = "FILA 3"
    else:
        fila = "Fila Especial"
    return fila
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
    #######---EJERCICIO 1---#######
    print ("EJERCICIO 1------------->")
    print ("Francisco Soto Vera")

#VARIABLES
diferenciaMax = 2
continuamos = False

#CODIGO
while not continuamos:
    #######---EJERCICIO 2---#######PEDIR NOTAS
    print ("EJERCICIO 2------------->")
    notaAntigua = float(input("Introduce la nota antigua:"))
    notaNueva = float(input("Introduce la nota nueva:"))

    #######---EJERCICIO 2.1---#######DIFERENCIA NOTA
    print ("EJERCICIO 2.1------------->")
    diferencia = diferenciaNumeros(notaNueva, notaAntigua)
    print ("La diferencia es %.2f." % diferencia)

    #######---EJERCICIO 2.2---#######Pregunta si esta seguro SI/NO
    print ("EJERCICIO 2.2------------->")
    if numeroMayorOtro(diferencia,diferenciaMax):
        segura = input("¿Estas segura? SI/NO:")
        if palabraIgualOtra(segura,"SI"):
            continuamos = True
            print ("He esrito si")
    else:
        continuamos = True
        print ("La diferencia es menor")

#######---EJERCICIO 3---#######
edad = int(input("Introduce tu edad:"))
apellido = input("Introduce tu apellido:")

if numeroMayorOtro(edad,18):
    #ASIGNAR SEGUN EL APELLIDO
    if letraEntreLetras(apellido[0].upper(),"A","G"):
        fila = "FILA 1"
    elif letraEntreLetras(apellido[0].upper(), "H","N"):
        fila = "FILA 2"
    else:
        fila = "FILA 3"
else:
    fila = "Fila Especial"

    
    






