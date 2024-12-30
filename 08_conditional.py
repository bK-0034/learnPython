#Conditionals
#Si se cummple la condición se ejecuta lo que está dentro de la condicional

my_condition= False

if my_condition: #Es lo mismo que: "If my_condition=True:""
    print("Se ejecuta la condición de if ")
    

my_condition = 5*3

if my_condition == 11: #Es lo mismo que: "If my_condition=True:""
    print("Se ejecuta la condición del 2do if ") 
else:
    print("Mi condición no es igual a 11")
    
print("La ejecución continúa...")

if my_condition > 11 and my_condition < 20: #Es lo mismo que: "If my_condition=True:""
    print("Se ejecuta la condición del 3er if ") ##No se está limitando
    
print("La ejecución continúa...")

#Comprobar si una cadena está vacía

my_string=''
if not my_string: #Verfica si my_string está vacio
     print("Esta cadena está vacia")
else: 
    print('No está vacia')


