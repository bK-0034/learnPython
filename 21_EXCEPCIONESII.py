#Capturas de varias excepciones
#Clausura Finally
#En el anterior solo se contemplo el error de la division entre 0, en este caso se agrega el error de ingresar letras
#Error (ValueError)
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
#CAMBIOS
#op1=(int(input('Introduce el primer número: ')))
#op2=(int(input('Introduce el segundo número: ')))
#operacion=(input('Introduce la operación a realizar (suma, resta, multiplicar o division): '))

while True:
    try: 
        op1=(int(input('Introduce el primer número: ')))
        op2=(int(input('Introduce el segundo número: ')))
        
        break
    
    except ValueError: 
        print('Esos valores no son correctos\t El programa continuará...')

operacion=(input('Introduce la operación a realizar (suma, resta, multiplicar o division): '))

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