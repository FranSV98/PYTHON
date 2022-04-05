#Calculadora V1
print ("CALCULADORA V1--------->\n")

print("¿Qué operación quieres realizar?")


def suma(a,b):
    return(a+b)

def resta(a,b):
    return(a-b)

def multiplicacion(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

def detecOpe():
    cadena = "+"
    letra = input
    if letra in cadena:
        print (suma(a,b))

    cadena = "-"
    letra = input
    if letra in cadena:
        print (resta(a,b))

    cadena = "*"
    letra = input
    if letra in cadena:
        print (multiplicacion(a,b))

    cadena = "/"
    letra = input
    if letra in cadena:
        print (division(a,b))










