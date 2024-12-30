##SETS 
#Definición
#Set es un tipo de dato
my_set= set()
#Con su constructor {}
#Primero indica que es un diccionario con las {}
my_other_set= {} #Da que es diccionario
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Kiscel", "Esquivel", 21}##Ya es set
print(type(my_other_set)) 

#Se lia con diccionario y sets {}

#Operaciones con SETS
print(len(my_other_set)) #Imprime que tiene 3 elementos (3)

## print(my_other_set[0]) error, no es lo mismo que la lista
##No se puede acceder a los elementos
#Set no es una estructura ordenada
my_other_set.add(21280673) ##Agrega al elemento 0 
#No hay control absoluto de los sets
#No hay listado, no puedes acceder al elemento 0, 1, 2
print(my_other_set)
my_other_set.add(21280673)
print(my_other_set)

#Un set no admite repetidos, las tuplas admiten repetidos, las list admiten repetidos
#No ordena por orden de entrada, ordena por un hass interno
#No son datos inmutables, se puede agregar elementos como en la lista

#Posibilidad de hacer busquedas
#Busca si hay Kiscel en el set, arroja true or false
print('Kiscel' in my_other_set) #verdadero, en el set hay Kiscel
print('kiscel' in my_other_set) #false, en el set no hay kiscel

#Así como se agregan datos, se pueden eliminar
my_other_set.remove('Kiscel')
print(my_other_set)#Elimina el nombre de Kiscel

#RESUME: NO PERMITE REPETIDOS Y NO ORDENA POR ELEMENTOS

my_other_set.clear()
print(my_other_set) ##Aroja el set limpio
print(len(my_other_set))#Arroja 0, pues, lo limpio en clear

##del es una palabra reservada del sistema
# a las acciones propias de un objeto accedemos con un punto
# del es una palabra reservada que se puede usar en todas las estructuras

del my_other_set
 #print(my_other_set) ##Ya no existe, se elimino con el del, por lo que Sintax Error
 
 #Convertir Set en Lista para poder modificar los datos y tener un orden
my_set={"Kiscel", "EM", 21}
my_list_one=list(my_set)
print(my_list_one)
print(type(my_list_one)) ##Set se hizo Lista
#Al pasarlo a una lista, ya tengo una estructura ordenada

print(my_list_one[0]) ##Imprimira 21, porque al ordenar la lista se hizo [21, EM, Kiscel]

my_other_set={'C++', 'Python', 'Java','Swift'}

#Unir Sets, ya no se utiliza + en sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)

##¿qué pasa si le vuelvo a agregar el mismo set?
print(my_new_set.union(my_new_set)) ##No pasa nada, imprime solo my_new_set
##Por qué no puede repetir, por eso no imprime doble vez

#De my_new_set le quita lo de my_set, da la diferencia
print(my_set)
print(my_new_set)
print(my_new_set.difference(my_set))
