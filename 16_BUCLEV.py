#continue, pass y else
for letra in 'Python':
    
    if letra=='h':
        continue #va a ignorar la letra h, por lo tanto se va a saltar la letra h, es decir, ignora la linea siguiente cuando llega a h
    print('Viendo la letra: '+ letra) #imprime viendo la letra P, viendo la letra Y, ...
    
#ejercicio2

nombre='Britany EM'
contador=0

for i in nombre: 
    if i== ' ':
        continue #va a saltar y no va a contar el espacio, sale del bucle for
    contador+=1

print(contador) #ya imprimio 9, solo contó las letras e ignora los espacios en blanco

#print(len(nombre))#imprime la longitud
#va a imprimir 10, sin embargo, son 9. Para que no cuente el espacio en blanco se hará lo siguiente