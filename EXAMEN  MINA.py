
import random

def generaTablero(cantidad, rango):
    tabl = []
    for x in range(cantidad):
        signo = ""
        num = random.randrange(0,rango)
        if num == 0:
            signo = "D"
        elif num == 1:
            signo = "O"
        elif num == 2:
            signo = "P"
        elif num == 3:
            signo = "N"
        else:
            signo = "C"
        tabl.append(signo)
    return tabl

def sorteo():
    empieza = 1
    num = random.randrange(2)
    print (num)
    if num == 1:
        empieza = 2
    return empieza

def imprimeTablero(tablero, desenterrados):
    print ("")
    print ("TABLERO\n")
    fila = 0
    itera = 0
    while fila < 5:
        for i in range(5):
            if itera in desenterrados:
                sig = tablero[itera]
                if ia == "s":
                    sig = "X"
            else:
                sig = " "
            print ("| "+sig+" ", end ="")
            itera +=1
        print ("|\n")
        fila +=1

def sumaPuntos(cas):
    jug = 0
    if cas == "D":
        jug = 5
    elif cas == "O":
        jug = 3
    elif cas == "P":
        jug = 2
    elif cas == "C":
        jug = -2
    print ("PUNTOS: ", end="")
    print (jug)
    return jug

def juegaTurno(jug):
    jugador = 0
    prueba = input("Turno de "+jug+": ")
    casilla = (int(prueba[0])*5-5)+int(prueba[1])-1
    print (casilla)
    desenterrados.append(casilla)
    print (tablero[casilla])
    jugador = sumaPuntos(tablero[casilla])
    imprimeTablero(tablero, desenterrados)
    return jugador

def juegaIA():
    ia = 0
    casillaIA = -1
    libre = False
    while libre == False:
        casillaIA = random.randrange(0,25)
        if casillaIA not in desenterrados:
            libre = True
    
    print("Turno de JUGADOR 2:")
    
    print (casillaIA)
    print (tablero[casillaIA])
    desenterrados.append(casillaIA)
    ia = sumaPuntos(tablero[casillaIA])
    imprimeTablero(tablero, desenterrados)
    return ia

    
#---------------------------------------------------------------------------
nombre = "Pablo de Cara Jiménez"
print (nombre)
print("\nPara introducir las coordenadas, escribe 2 dígitos segidos.\nPor ejempo \"24\" para [2,4]\n")

jugador1 = 0
jugador2 = 0

tablero = generaTablero(25,5)
desenterrados = []

ia = input ("Quiere jugar contra la IA? (s/n): ")

imprimeTablero(tablero, desenterrados)
turno = sorteo()
termina = "n"
print ("Comienza el Jugador " + str(turno))
if ia != "s":
    while jugador1 < 10 and jugador2 < 10:
        print ("JUGADOR 1: " + str(jugador1))
        print ("JUGADOR 2: " + str(jugador2))
        
        if turno%2 != 0:
            jugador1 = jugador1 + juegaTurno("JUGADOR 1")

        elif turno%2 == 0:
            jugador2 = jugador2 + juegaTurno("JUGADOR 2")
            
        turno = turno + 1

else:
    while jugador1 <= 15 and jugador2 <= 15 and termina != "s":
        print ("JUGADOR 1: " + str(jugador1))
        
        if turno%2 != 0:
            jugador1 = jugador1 + juegaTurno("JUGADOR 1")
            print ("JUGADOR 1: ", end="")
            print (jugador1)
            termina = input("Quieres parar? (s/n): ")

        elif turno%2 == 0:
            jugador2 = jugador2 + juegaIA()
            if jugador2 >=9 and jugador2 <=12:
                prob = random.randrange(0,10)
                if prob < 3:
                    termina = "s"
        turno = turno + 1

if ia != "s":
    print ("JUGADOR 1: " + str(jugador1))
    print ("JUGADOR 2: " + str(jugador2))
    if jugador1 >= 10:
        print ("JUGADOR 1 GANA!!!")
    else:
        print ("JUGADOR 2 GANA!!!")

else:
    print ("JUGADOR 1: " + str(jugador1))
    print ("JUGADOR 2: " + str(jugador2))
    if jugador1 > 15 or jugador1 < jugador2:
        print ("JUGADOR 2 GANA!!!")
    elif jugador2 > 15 or jugador2 < jugador1:
        print ("JUGADOR 1 GANA!!!")
    else:
        print ("EMPATE!!!")





