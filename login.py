import base64, re, getpass
from base_datos import db_ecommerce
class Logeo():
    def __init__(self):
        
        self.__email=""
        self.__password=""
        self.__nombre=""
        self.__id=""

    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_nombre(self):
        return self.__nombre
    def get_id(self):
        return self.__id
    def set_email(self, email):
        self.__email=email

    def login(self):
        validacion=False
        while not validacion:
            self.__email=input("Ingrese email: \n")
            clave=getpass.getpass("Ingrese la contraseña :\n" )
            #clave=input("Ingrese contraseña: \n ")
            query="Select user_id,nombre, contrasenia from usuarios  where email=%s"
            val=(self.__email,)
            db_ecommerce.get_cursor().execute(query, val)
            resultado=db_ecommerce.get_cursor().fetchone()
            if resultado is not None:
                validacion=True
                self.__id=resultado[0]
                self.__nombre=resultado[1]
                encriptada=base64.encodebytes(bytes(clave,"utf-8")).decode("utf-8")[:-1]
                if encriptada==resultado[2]:
                    print("Ingreso exitoso!")
                    input("Presione enter para continuar...")
                    
                else:
                    print ("El email/contraseña  ingresados no coinciden ")
            else:      
                print("El email o contraseña  ingresados no se encuentran  registrados ")

    def logout(self):
        self.__email=""
        print("La sesión se cerró con éxito")
        input("Presione enter para continuar")


                
            
user=Logeo()
#user.login()




        


        