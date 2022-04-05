def esNumeroUnString(n):
    esNumero = True
    numeros = "1234567890"
    if n[0] == "-":
        n = n[1:]
    for i in n:
        if i  not in numeros:
            esNumero = False
    return esNumero

def funPedirNumeros():
    listaNumeros = []
    esNumero = True
    while esNumero:
        num = input("Introduce un número: ")
        esNumero = esNumeroUnString(num)
        if esNumero:
            listaNumeros.append(int(num))
    return listaNumeros

def contarPositivos():
    pos_count, neg_count = 0, 0
    for num in contarPositivos:
        if num >= 0: 
            pos_count += 1
  
        else: 
            neg_count += 1
    print(pos_count) 
    print(neg_count) 


esNumeroUnString(n)
funPedirNumeros()
contarPositivos()



    



    

    
    








    


    
