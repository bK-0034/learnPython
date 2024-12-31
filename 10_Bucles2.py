for i in ['Kiscel', 'Mecatrónica', '3']:
    print ('Hola', end=' ') #imprime tanto Holas tanto número de elementos haya en el argumento del for
    
#también puede ser: for i in britany04@gmail print ('Hola', end=' ' ) imprimira tantos holas como tantos caracteres haya en el cadena
#con esto se puede verificar si un correo es correcto 

#ejemplo 
email=False

for a in 'britanygmail.com':
    if(a=='@'):
        email=True

if email==True: #Es lo mismo poner if email: --> esto quiere decir que email==true, está implicito
    print('Correo correcto, felicidades')
else:
    print('Sorry, its wrong')
    #== -->compara
    #= -->iguala, es diferente hay que tenerlo en cuenta
    
#USO DE RANGE
for i in range(5):
    print('Holaaa') #imprimirá 5 veces Holaaa, hace un array de holas 
    
