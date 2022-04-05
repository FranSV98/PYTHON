# Diccionario -> Ordenado + Modificables + No duplicado.
colores = {
    "Rojo":3,
    "Naranja":1,
    "Amarillo":1,
    "Verde":2,
    "Azul":5,
    "Morado":0
}

print("\n· Imprime el diccionario entero.")
print(colores)

print("\n· Imprime solo las llaves de un diccionario.")
print(colores.keys())

print("\n· Imprime solo los valores de un diccionario.")
print(colores.values())

print("\n· Imprime una lista de listas con los valores.")
print(colores.items())

# Acceso a datos

print("\n· Acceso a datos 1.")
print(colores["Verde"])

print("\n· Acceso a datos 2.")
print(colores.get("Verde"))

# Operar con valor

print("\n· Operar con un valor de un diccionario.")
valor = colores.get("Verde")

if valor == 2:
    print("Jejeje ... Siuuu")

print("\n------------------------------------")
print("valor = colores.get('Verde')\n\nif valor == 2:\n\tprint('Jejeje ... Siuuu')")
print("------------------------------------")

marca = {
    "BMW",
    "FORD",
    "FERRARI",
    "CHEVROLET",
    "RENAULT"
}

# Buscar

print("\n· Imprime un booleano si está en el diccionario o no.")
busqueda = "BMW" in marca
print(busqueda)

notas = {
    "LMG":[6, 4, 3]
}

# Impresión

print("\n· Imprimir un valor de una lista de un diccionario.")
print(notas["LMG"])
print(notas["LMG"][0])

# Actualizar

print("\n· Actualizar un valor de una clave.")
colores.update({"Morado":2})
print(colores["Morado"])

# Añadir

print("\n· Para añadir llaves.")
# Se pueden añadir listas
# Se pueden añadir variables
marca.add("KIA")
print(marca)

# Unión

print("\n· Para unir diccionarios.")
seta = {"asd", "das"}
setb = {"jeas"}
setc = seta.union(setb)
print(setc)
# Suprime duplicados
# Intersection coge  solo los elementos que se encuentran en los dos sitios
setc = setb.intersection(seta)
print(setc)
setd = {"asd", "kojio"}
setc.update(setd)
print(setc)

# Eliminar

print("\n· Para eliminar keys.")
print("\nHay varias maneras de hacerlo:\n- marca.discard('FORD')\n- marca.remove('RENAULT')\n- marca.pop('KIA')\n- marca.clear()\n")
marca.discard("FORD")
print(marca)
marca.remove("RENAULT")
print(marca)
print("\n# El pop elimina el último elemento añadido.")
marca.pop()
print(marca)
marca.clear()
print(marca)

# Eliminación de diccionarios

print("\n· Para eliminar directamente el diccionario se hace con el del.")
print("del marcas")

# Bucles

print("\n· For en un set.")
set = {"jaja", "jeje", "jiji", "jojo", "juju"}

for i in set:
    print(i)

print("\n· For en un diccionario.")

print("\nImpresión de llaves 1.")
for i in colores:
    print(i)

print("\nImpresión de llaves 2.")
for i in colores.keys():
    print(i)

print("\nImpresión de valores 1.")
for i in colores:
    print(colores[i])

print("\nImpresión de valores 2.")
for i in colores.values():
    print(i)


print("\nImpresión de clave y valor 1.")
for i in colores:
    print(i, colores[i])

print("\nImpresión de clave y valor 2.")
for clave, valor in colores.items():
    print(clave, valor)