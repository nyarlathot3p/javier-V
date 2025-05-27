usurios={"usuario1":"pass1",
         "usuario2":"pass2",
         "usuario3":"pass3",}

usuario1="test1"
usuario2="test2"
usuario3="test3"
pass1="pass1"
pass2="pass2"
pass3="pass3"
iniciado=False
numerovalido=False


#menu

def menu():
    while True:
        try:
            opcion=int(input('''elija una opcion
                        1- iniciar sesión
                        2- registrar usuario
                        3- salir
                    '''))
            return(opcion)
            break
        except Exception:
            print("favor elegir una opcion valida")

def menu2():
    while True:
        try:
            opcion=int(input('''elija una opcion
                        1- realizar llamada
                        2- enviar correo electronico
                        3- cerrar sesión
                    '''))
            return(opcion)
            break
        except Exception:
            print("favor elegir una opcion valida")

def ingreso(usuar,usuarios,passwd):
    if passwd==usuarios[usuar]:
        print("bienbenido")
        iniciado=True
        return(true)
    else:
        print("el usuario y la clave no coinsiden")


match menu():
    case 1:
        user=input("usuario: ")
        if user not in (usurios):
            print("usuario no existe,si no tiene usuario, primero debe registrarce")
            menu()
        elif user in (usurios):
            password=input("ingrese su clave: ")
            ingreso(user,usurios,password)
        
        if iniciado==True:
            while True:
                match menu2():
                    case 1:
                        while numerovalido==False:
                            try:
                                num=int(input("ingrese el telefono"))
                            except Exception:
                                print("numero no valido")
                            if len(str(num))==9 and num[0]==9:
                                numerovalido=True
                    case 2:
                        correo=input("ingrese correo al que enviara el email  ")
                        while "@" not in correo:
                            print("debe ingresar un correo valido")
                            correo=input("ingrese correo al que enviara el email  ")
                        mensaje=input('''escriba du mensaje
                                    
                                    ''')
                    case 3:
                        iniciado=False
                    case _:
                        print("opcion invalida")

                    
                    
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("ingrese una opcion valida")

