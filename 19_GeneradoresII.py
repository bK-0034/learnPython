#Nueva instrucció Yield From
#Simplifica el código en el caso de utilizar bucles anidados, como un for dentro de otro for. 
#EJEMPLO... Crear una función que devuelva ciudades

def devuelve_Ciudades (*ciudades): #cuándo se pone el asterico, indica se van a ingresar un número indeterminado de elementos
    #los elementos los va a recibir en forma de tupla
    #recorrer elementos de la tupla: 
    for elemento in ciudades:  #Bucle for padre/principal
        for subElemento in elemento: #bucle for anidado
            # yield elemento 
            yield subElemento #va imprimir las letras(subelementos de los elementos(letras))
ciudades_Devueltas=devuelve_Ciudades("México", 'Monterrey', 'Berlín', 'Zacatecas', 'Valhalla')

#otra manera de utilizar el yield from es:  #funciona igual a como está arriba
def devuelve_Ciudades2 (*cities): 
    for elemento in cities: 
        yield from elemento
ciudades2=devuelve_Ciudades2('Moscú','Reeves','Bon Jovi')

print(next(ciudades2))
print('Código 1;')
print(next(ciudades2))
print('Codigo 2;')
print(next(ciudades2))
print('Codigo 3;')
print(next(ciudades2))
print(next(ciudades2))
print(next(ciudades2))

##cada ciudad está compuesto por subelementos, que son las letras, para acceder a ellos hay que usar yield from. 
    