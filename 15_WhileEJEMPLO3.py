import math
print('Programa para calcular la raíz cuadrada de un número ')

num=int(input('Introduce el número, por favor'))
intentos=0

while num<0: 
    print('No se puede hallar la raíz de un número negativo')
    
    if intentos==2:
        print('Has intentado muchos intentos, el programa ha finalizado')
        break; #sale del programa 

    num=int(input('Introduce el número, por favor'))
    if num<0: 
        intentos=intentos+1

if intentos<2: 
    solucion=math.sqrt(num)
    print('La raíz cuadrada de '+ str(num) + ' es ' + str(solucion))

intentos=0

