def subeNotas (porcentaje,x):
    notasBien = []                                      # Sube cada nota un porcentaje
    for i in x:
        i = i + i*porcentaje/100
        notasBien.append (i)
    return notasBien

def difSubida (notas, notasBien):
    difSubidas = []                                     # Calcula la diferencia de cada nota
    pos = 0
    for j in notasBien:
        difSubidas.append (notasBien[pos]-notas[pos])
        pos += 1
    return difSubidas

def mediaSubida (gg):
    num = len (gg)                              # Calcula la media de subida
    suma = sum (gg)
    manolo = suma/num
    return manolo

def sinSuspensos (asignaturas, notas, notasBien):
    posN = 0                                            # Elimina de las listas
    for k in notasBien:                                 # los elementos suspensos
        if k < 5:
            asignaturas.remove (asignaturas[posN])
            notas.remove (notas[posN])
            notasBien.remove (notasBien[posN])
        posN += 1

def boleton (asignaturas, notas, notasBien):
    boletin = []                                        #Imprime el ÚNICO y GENUINO boletín
    posB = 0
    for l in asignaturas:
        print ("| \t %s \t | \t %d \t | \t %.1f \t |" % (asignaturas[posB], notas[posB], notasBien[posB]))
        posB += 1


#...............................................................................

nombre = "Pablo de Cara Jiménez"
print (nombre)

asignaturas = ["LM", "ED", "Prog", "SI", "BD", "FOL"]
notas = [7,3,9,8,8,4]

notasBien = subeNotas (20, notas)
print ("Las notas correctas son:")
print (notasBien)

difSubidas = difSubida (notas, notasBien)
#print (difSubidas)
media = mediaSubida (difSubidas)
#print ("La media de la subida de notas es %.1f" % media)

aprobadas = sinSuspensos (asignaturas, notas, notasBien)
#print ("Las asignaturas aprobadas son:")
#print (asignaturas)
print ("")
print ("\t \t \tBoletín")
print ("")
boletin = boleton (asignaturas, notas, notasBien)
print ("")
salir = input ("Presione Enter para salir") 		# Esto es solo para que no salga automáticamente
