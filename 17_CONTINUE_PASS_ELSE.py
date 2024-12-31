email=input('Ingresa tu correo electrónico: ')

for i in email: 
    if i=='@': 
        arroba=True
        break; #saldrá del bucle de for, por lo tanto brincará a imprimir el arroba
else: 
    arroba=False
    
print(arroba)