#Listas == Conjunto de datos, cada uno en una posición
#maneras de definir listas
#proporciona operaciones de listas
#ordenar, reverses, insertar elementos
#en las listas se pueden repetir elementos

# el array es una estructura que no se puede mover como una lista

my_list= list()
my_other_list=[]

print(len(my_list)) 
# puede ser un array de elementos
#forma de agrupar datos siguiendo un orden
my_list = [4, 24, 62, 30, 17] #esto es un array de elementos
print(my_list)
print(len(my_list))

my_other_list=[21, 1.57, 'Tany' ]
print(type(my_other_list))

#imprimir un elemento de la lista
print(my_other_list[1]) #va a imprimir mi altura
print(my_other_list)
#Operaciones especiales
#COUT 
print(my_other_list.count('Tany'))#Cuantos Tany hay en la lista

age, height, name = my_other_list
print(name)

#Juntar listas
print(my_list + my_other_list)

#Agregar elementos a las listas al final
my_other_list.append('Kiscel')
print(my_other_list)

#Agregar elementos a las listas en un orden determinado
my_other_list.insert(3, 'Srita')
print(my_other_list)

#Eliminar valores/elementos de una lista
my_other_list.remove(21)
print(my_other_list)

#Elimina el último dato
my_other_list.pop()
print(my_other_list)

#Qué hace pop? se le pasa el dato del elemento
#que se quiere desapilar
print(my_other_list.pop())

my_list='Hola Python' #Esto ya no es una lista
print(type(my_list)) #ha cambiado el tipo de dato

bk_list=[21, 40, 50, 67]
print(bk_list)
#INSERTAR EN LAS LISTAS
bk_list.insert(0, 90)
print(bk_list)
#REASIGNAR VALORES A LA LISTA
bk_list[0]=45
print(bk_list)

#Cambiar orden
bk_list.reverse()
print(bk_list)

#ORDENAR LA LISTA, ASCEDENTE
bk_list.sort()
print(bk_list)

