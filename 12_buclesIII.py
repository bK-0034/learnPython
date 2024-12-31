#TIPO RANGE, NOTACIÓN ESPECIAL PARA FUNCIÓN PRINT 
for i in range(5): #son 5 elementos comenzando desde el 0, es decir del 0 al 4
    print(i)
    
#FUNCIÓN DE TIPO F (en el print)
for i in range(8):
    print(f'Valor de la variables {i}') #concatena el texto con el valor de la variables en cada vuelta de bucle
    #valor de la variable 0
    #valor de la variable 1
    #valor de la variable 2
    #valor de la variable 3 y así lo concatena seguido 
    
#hacer que cuenta en deteerminado valor hasta otro valor
for i in range(12,15): #de 12 al 14, no considera el 15, es el limite superior no lo toca
    print(f'Este es el otro bucle {i}')

#range con un tercer argumento (indica de cuánto en cuánto se deberá contar)

for i in range (30,50,10): #no considera el 50 
    print(f'Uno más {i}')