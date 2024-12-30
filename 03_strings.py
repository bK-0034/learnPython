##Definir
my_string='Máquina' 
my_other_string="Máquina de guerra" 

#Imprimir el número de caracteres
print(len(my_string)) #7
print(len(my_other_string)) #17
# Concatenar cadenas
print(my_string+'  '+ my_other_string)

my_new_line='Este es un String\ncon salto de linea'
print(my_new_line) #Escribir con salto de linea
#Con tabulación 
my_tab_line='Este es un String\tcon tabulación'
print(my_tab_line)
#Con escapado
my_scape_line='\tEste es un String\n con salto de linea'
print(my_scape_line)
#se puede cancelar el tabulado y los demás con \\t o \\n

#formatear strings
print('Meine name ist Kiscel')
name, lastname, age='Kiscel','EM', 21 #ya está definido
print('Meine name ist {} {} und ich bin {} Jahre alt'.format(name, lastname, age))
print('Meine name ist %s %s und ich bin %d Jahre alt'%(name, lastname, age))
print(f'Meine name ist {name} {lastname} und ich bin {age} Jahre alt')

#Desempaquetado de caracteres
languaje='python'
a,b,c,d,e,f=languaje
print(a)
print(b)

#división
languaje_slice = languaje[1:3]
print(languaje_slice) #la letra T es la 3ra de PYTHON y la 1 es la Y
languaje_slice = languaje[-2]
print(languaje_slice)
#imprimir al reverso python = nohtyP
reverse_languaje= languaje[::-1]
print(reverse_languaje)

#hacer saltos, para evitar caracteres
languaje_slice = languaje[0:6:2] #PTO considera del 0 al 6 y va saltando cada 2
print(languaje_slice)

#Funciones del sistema (predeterminadas)
print(languaje.capitalize()) #MAYÚSCULAS (la primera)
print(languaje.upper()) #todas en mayúsculas
print(languaje.count('t'))#cuenta cuantas t minusculas hay en python =1
print(languaje.isnumeric()) #arroja False porque no es número
print(languaje.lower())#todas minúsculas
print(languaje.upper().isupper())#se pueden combinar
print(languaje.startswith('py')) #pregunta si languaje empieza con py es true
