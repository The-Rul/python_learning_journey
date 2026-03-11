''' Ejercicio 2: Validar email
2. Validar email. Funcion pasamos un mail dice si es correcto 
    Validaciones:
    - No puede tener espacios en blanco dentro del email. 
        -Quitarlos con split. Y replace.
    - Solo  debe tener una @.
    - Después de la @ debe haber al menos un punto. 
    - Entre la  @ y el punto tiene que haber mínimo 2 caracteres.
    - Después del último punto tiene que haber entre 2 y 5 caracteres.  
'''  
'''
def validate_email(email):
    print(email)
    # Eliminar espacios en blanco
    email = email.strip()
    error = False
    msn = ""
    # 1. Error si hay espacios en blanco dentro del email
    if " " in email:
        error = True
        msn += "El email no puede contener espacios en blanco. \n "
    if email.count("@") != 1:
        error = True
        msn += "El email debe contener exactaente una @. \n "
    
    arroba = email.find("@") #Index de la arroba
    print(f"Arroba:{arroba}")
    print(email[arroba::]) # Sumar uno a "arroba" para no tener la arroba.

    if "." not in email[arroba::]:
        error = True
        msn += "Sin punto despues de la arroba "
        
    #Entre la  @ y el punto tiene que haber mínimo 2 caracteres.
    punto = email[arroba::].find(".")  
    print(f"punto:{punto}")
    print(f"arroba-punto: {email[arroba:arroba+punto:]}")
    
    if len(email[arroba:punto:]) < 2:
        error = True    
        msn += "Entre @ y . debe haber al menos 2 caracteres"
    
    # Despues del punto entre 2 y 5 caracteres
    if len(email[arroba+punto::]) < 2 or len(email[punto::]) > 5:
       error = True
       msn += "Despues del punto debe haber entre 2 y 5 caracteres"   
    
    if error:
        print(f"{error}: email incorrecto.")
        print(msn)
    else:
        return print("Email correcto")
'''   
# Testeos: 
email = "user@example.com" # Correcto
email_1 = "user @example.com" # Contiene espacio
email_2 = "userexample.com" # No contiene @   
email_3 = "user@domain" # No contiene . despues de @
email_4 = "user@d.com" # NMenos de 2 caracteres entre @ y .
email_5 = "user@domain.commmmmmmm" # Después del punto más de 5 caracteres   
email_6 = "user @d.coommmmm"
#validate_email(email_1)


'''Alternativa. Correccion profe. '''
print("-"*30)
print("PROFE CORRECTION")
print("-"*30)

def validate_email_profe(email):
    # Podemos devolver dos cosas un booleano y el mensaje de error
    email_correcto = True
    mensaje_error = "\n"
    # 1. Eliminar espacios a izq y drch. 
    email = email.strip()
    
    # 2. Comprobar espacios en blanco dentro del email
    if email.count(" ") > 0:
        email_correcto = False
        mensaje_error = "\t - El email no puede contener espacios en blanco. \n"
    
    # 3. Comprobar que solo hay una @
    if email.count("@") != 1:
        email_correcto = False
        mensaje_error += "\t - El email debe contener exactamente una @. \n"
    else:   
        # 4. Después de arroba al menos 1 punto. (Chequear si hay arroba)
        pos_arroba = email.find("@") #Sacar index de la arroba en el string
        dominio = email[pos_arroba + 1:] # Substring a partir de la arroba. (sumar 1 para evitar el @)
        print (f"Dominio: {dominio}")
        if (dominio.count(".") < 1): # Contar si hay 
            email_correcto = False
            mensaje_error += "\t -Email debe tener . despues @."
    
        # 5. Ver si hay 2 o menos caracteres entre @ y . 
        if (dominio.find(".") <  2):
            email_correcto = False
            mensaje_error  += """\t - Hay menos de 2 caracteres entre la arroba y el punto. \n""" # """ para que recoga las dos lineas de string7

        # 6. Si despues del punto hay entre 2 y 5 caracteres.
        if (len(dominio[dominio.rfind(".") + 1:]) < 2 or len(dominio[dominio.rfind(".") + 1:]) > 5):
            subdominio = dominio[dominio.rfind(".") + 1:]
            print(f"Subdominio: {subdominio}")
            email_correcto = False
            mensaje_error += """\t - Lo de despues del punto debe ser entre 2 y 5 caracteres.  \n""" # """ para que recoga las dos lineas de string7
            

            
    
    
    # Devolver variables
    return email_correcto, mensaje_error   
    

# TESTEOS
#email = input("Introduce tu email: ")
email_list = [email,email_1, email_2, email_3, email_4, email_5, email_6]
for email in email_list:
    print(f"Email: {email}")
    email_correcto, mensaje_error = validate_email_profe(email)
    #print(email_correcto, mensaje_error)
    if email_correcto:
        print("Email correcto")
    else:
        print(f"El correo es erroneo porque: {mensaje_error}")
    print("-"*30)
# Recibir los objetos que devuelve la función e imprimirlos

