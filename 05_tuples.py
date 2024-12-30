##TUPLES: CONJUNTOS DE VALORES
#Estructura fija de valor, no se puede modificar
#solo por número de elementos en diferentes lenguajes
#DEFINIR TUPLA
my_tuple= tuple()
my_other_tuple=()

my_tuple=(21, 1.57, 'kiscel', 'esquivel')
my_other_tuple=(60, 30)
#Si se pueden sumar, no se puede modificar pero si las suma
my_sum_tuple=my_other_tuple + my_tuple
print(my_sum_tuple)

print(type(my_tuple))  
#Imprimir elementos de la tupla, como en las listas
print(my_tuple[0])
print(my_tuple[-1])
##Ya no hay operaciones de inserción
#COUNT --> contar cuantos elementos hay ()
print(my_tuple.count(21)) ##arrroja 1, pues solo hay 1 21 en la lista
print(my_tuple.index(21)) #indica dónde está el indice del 21, en la tupla está en el lugar 3
print(my_tuple.index('kiscel')) #Indica donde está en el indice

#En las tupas no podemos agregar como en las listas
#La tuplas es inmutable
#No hay operación insert 
#Para imprimir un "conjunto" de la tupla
print(my_sum_tuple[1:6])#imprime del 1 al 5, no considera el 6

##TUPLA CON VALORES CONSTANTES
#TUPLA MUTABLE O LISTA?? 
#Reasignar la tupla a lista
my_tuple= list(my_tuple)
print(type(my_tuple))

my_tuple[2]='ELECTROMAC'
my_tuple.insert(1, 'azul')
print(my_tuple)

#Del (borrar) Incoherente, por ser tupla, pero existe
