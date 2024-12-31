mi_Email= input("Ingresa tu correo electrónico:")
email= False
for i in mi_Email:
    if (i=='@'):
        email=True

if email: 
    print ("Correo correcto")
else: 
    print ("Correo inválido")
        