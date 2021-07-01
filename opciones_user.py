from login import user
from base_datos import db_ecommerce
from validacion import check
import base64, getpass
import os

class Opciones_user():
    def __init__(self):
        self.__seleccion=""
        self.__new_passw=""
    
    def get_seleccion(self):
        return self.__seleccion
    def get_new_passw(self):
        return self.__new_passw

    def set_seleccion(self, seleccion):
        self.__seleccion=seleccion
    def set_new_passw(self, password):
        self.__new_passw=password
        
    
    def seleccionar_opcion(self):
        os.system('cls')
        print("Seleccione la opción deseada ")
        print("1. Modificar contraseña")
        print("2. Eliminar cuenta")
        valido=False
        while not valido:
            try:
                seleccion=int(input("Seleccione: "))
            except:
                print("Seleccione una opción valida! ")
            if seleccion>=1 and seleccion<=2:
                valido=True
                self.__seleccion=seleccion
            else:
                print("Seleccione una opción valida! ")
                 
    def modificar_password(self):
        
        valido=False
        while not valido:
            os.system('cls')
            self.__new_passw=getpass.getpass("Ingrese una nueva  contraseña :\n" )
            #self.__new_passw=input("Ingrese una contraseña :\n" )
            enc_passw = base64.encodebytes(bytes(self.__new_passw,"utf-8")).decode("utf-8")[:-1]
            if enc_passw==user.get_password():  
                print("La contraseña introducida es igual a la anterior. Por favor, cambiela!")
                input("presione enter para continuar...")
            else:
                valido=check.check_password(self.__new_passw)
                if not valido:
                    print("La contraseña debe contener al menos 8 caracteres, una letra mayuscula, una minuscula, un digito y algunos de los siguientes caracteres (?=.*?[#?!@$%^&*-]) \n ")
                    input("presione enter para continuar...")
                else:
                    valido=False
                    ver_password=getpass.getpass("Ingrese nuevamente la contraseña :\n" )
                    #ver_password=input("Ingrese nuevamente la contraseña :\n" )
                    if self.__new_passw==ver_password:
                        self.__new_passw=base64.encodebytes(bytes(self.__new_passw,"utf-8")).decode("utf-8")[:-1]
                        valido=True
                        query="update usuarios set contrasenia=%s where email=%s"
                        val=(self.get_new_passw(), user.get_email())
                        db_ecommerce.get_cursor().execute(query, val)
                        db_ecommerce.conexion.commit()
                        print("La contraseña se ha cambiado con éxito")
                        input("Presione enter para continuar...")
                    else:
                        print("Las contraseñas  ingresadas no coinciden, intente nuevamente  ")
                        input("presione enter para continuar...")

    def eliminar_cuenta(self):
        print(f"La cuenta asociada al email {user.get_email()} esta a punto de ser eliminada. Desea continuar? Si/No ")
        valido=False
        while not valido:
            respuesta=str(input("Ingrese su respuesta:  \n "))           
            if respuesta.lower()=="si" or respuesta.lower()=="no":    
                valido=True  
                if respuesta=="si":
                    query="delete from usuarios where email=%s"
                    val=(user.get_email(),)
                    db_ecommerce.get_cursor().execute(query, val)
                    db_ecommerce.conexion.commit()
                    print("La cuenta ha sido eliminada")
                    user.logout()
                else:
                    print("La cuenta NO ha sido eliminada")
                    input("Presione enter para continuar...")
            else:
                print("Ingrese una opción valida")

user_options=Opciones_user()
    