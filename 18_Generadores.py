#¿Qué son los generadores? Son estructuras que extraen valores de una función y se almacenan en objetos iterables(que se pueden recorrer)
#Estos valores se almacenan de uno en uno
#Cada vez que un generador almacena un valor, este permanece en un estado pausado hasta que se solicita el siguiente. 
#"Suspensión de estado"
#se van generando uno a uno elementos

#Práctica: Función que genere números pares: 

def genera_Pares(limite): #el "limite" va a limitar cuántos numeros pares se van a generar
    num=1
    mi_Lista=[] #esto es una lista
    
    while num<limite:
        #mi_Lista.append(num*2) #se estará llamando a que genere numeros pares cada que se le llame
        yield num*2 #función de generación
        num+=1 
    #return mi_Lista --> la instrucción no se utiliza ya que estamos utilizando la instrucción YIELD
    #ENTRE LLAMADA Y LLAMADA ENTRA EN UN ESTADO DE SUSPENSIÓN
devuelve_Pares=genera_Pares(10)
print(next(devuelve_Pares)) #imrpime 2
print('Aquí podría ir más código..')
print(next(devuelve_Pares)) #imprime 4
print('Aquí podría ir más código...')
print(next(devuelve_Pares)) #se llama constantemente, por lo que se está actualizando el generador
print('Aquí aún más código...') #imprime 6
#print(genera_Pares(10)) #imprimirá 10 números pares --> va junto return

