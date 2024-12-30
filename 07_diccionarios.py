##Diccionarios##
#Mapas, hasmaps = igual
#hasmap diferente del diccionario a nivel de propiedades 

#Definición
my_dict=dict() #Forma número 1
my_other_dict={} #Forma número 2
print(type(my_dict)) #Dará que es diccionario
print(type(my_other_dict)) #Dará que es diccionario

my_other_dict = {"Nombre": "Kiscel", 'Apellido':'Esquivel', 'Edad':21, 1:"Python"}
#Si separamos con comas dentro de las llaves en un set
#Por lo tanto se requiere de algo nuevo
#Se meten los mismos datos, pero se está agrupando
#Relación clave - valor

#Se debe definir de qué tipo será la clave y de qué tipo será el valor

my_dict={
    "Nombre": "Kiscel",
    'Apellido':'Esquivel', 
    'Edad':21, 
    'Lenguajes':{"Python", 'Swift','Java','Ladder'},
    1:'21280673'
    } #En lenguaje tenemos una clave con un elemento set. 
print(my_other_dict)
print(my_dict)

#Tipo de estructura con la que podemos almacenar datos clave-valor

#Imprime cuántas relaciones clave-valor hay dentro del diccionario
print(len(my_dict))#5
print(len(my_other_dict))#4

#Entre corchetes se llama al valor de la clave
#En el ejemplo va a imprimir Kiscel, porque es el valor de Nombre
print(my_dict['Nombre'])

my_dict['Nombre']='Britany'#Actualizar el valor
#búsqueda de clave-valor
print(my_dict['Nombre'])
print(my_dict[1])#imprimirá el valor que tiene la clave 1

#Inserción de clave-valor
my_dict['Musik']='Rammstein' #Al final agregará Musik : Rammstein
print(my_dict)

#Eliminar una clave-valor del diccionario=Se utiliza del

#del my_dict['Apellido'] #Ya no aparecerá la clave y valor Apellido
#print(my_dict)

#Algo del que se carga no se puede recuperar
#Va al tiempo de ejecución

#Búsqueda de claves
print('Britany' in my_dict) #FALSE, BRITANY NO ES CLAVE
print('Apellido' in my_dict)#TRUE, APELLIDO ES CLAVE
print('Nombre' in my_dict)#True, SE BUSCA POR CLAVE, NO POR VALOR

#operaciones con diccionarios
#menciona que es un objeto
print(my_other_dict.items()) #agrupa en parentesis clave-valor
print(my_other_dict.keys()) #nos da las claves en los diccionarios, nos da un listado de las keys
print(my_other_dict.values()) #nos da el valor en el diccionario FORMATO LISTA EN CORCHETES

#Crear un diccionario, apartir de una lista. FROMKEYS SIRVE PARA CREAR DICCIONARIOS
my_list=["Nombre",1,"año"] #se convertirán en claves
my_other_new_dict=dict.fromkeys(my_list)
print(my_other_new_dict) 

#otra manera de crear un diccionario
my_second_dict=dict.fromkeys(("Graduación", "Pago", "Salón"))
print(my_second_dict)

#fromkeys, se le pueden pasar diferentes claves
#print(my_other_dict.fromkeys(("Nombre",1)))

#crea un diccionario SIN VALORES (FROMKEYS), pero no conserva los datos
#no sirve no reutiliza 
my_new_dict=my_other_dict.fromkeys(("Nombre",1,"piso"))
print(my_new_dict)

#Ahora el fromkeys se le pasará un diccionario completo
my_new_dict=dict.fromkeys(my_dict)
print(my_new_dict) #se hace una copia del diccionario que solo se queda con las claves
#ya después uno se encargará de meterle datos para su ejecución 

#my_new_dict = dict.fromkeys(my_dict, "BK", "SEVENFOLD")
#print((my_new_dict)) no tiene sentido esto, 

my_values=my_new_dict.values()
print(type(my_values)) #No es un listado ni un diccionario, es un dict_values
