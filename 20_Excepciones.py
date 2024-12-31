#EXCEPCIONES, ¿Qué son las excepciones? Son errores que ocurren durante la ejecución del programa.
#La sintaxis del código es correcta, pero durante la ejecución ha ocurrido algo inesperado. 
#las excepciones se pueden controlar para la ejecución del programa continúe. Esto se conoce como manejo o control de excepciones

def suma (num1, num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicar(num1, num2):
    return num1*num2

def division(num1, num2):
    #MANEJO DE LA EXCEPCION
    try:
        return num1/num2
    except ZeroDivisionError: 
        print ('Impossible')
        return('Operación erronea')

op1=(int(input('Introduce el primer número: ')))
op2=(int(input('Introduce el segundo número: ')))
operacion=(input('Introduce la operación a realizar (suma, resta, multiplicar o division): 5'))

if operacion=='suma':
    print(suma(op1, op2))
elif operacion == 'resta': 
    print(resta(op1, op2))
elif operacion=='multiplicar': 
    print(multiplicar(op1, op2))
elif operacion== 'division':
    print(division(op1, op2))
else: 
    print('Operación no contemplada')
    
print('Operación ejecutada...')
print('Final de programa...')