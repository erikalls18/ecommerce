
import base64, re, getpass
from base_datos import db_ecommerce
from validacion import check
from ubicacion import city
class New_User():
    def __init__(self):
        self.__id=0
        self.__nombre=""
        self.__email=""
        self.__password=""
        self.__ciudad=""
        self.__provincia=""
        self.__pais=""
    
    def get_nombre(self):
        return self.__nombre
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_ciudad(self):
        return self.__ciudad
    def get_provincia(self):
        return self.__provincia
    def get_pais(self):
        return self.__pais
    def get_id(self):
        return self.__id

    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_email(self,email):
        self.__email=email
    def set_password(self,password):
        self.__password=password
    def set_ciudad(self,ciudad):
        self.__ciudad=ciudad
    def set_provincia(self,provincia):
        self.__provincia=provincia
    def set_pais(self,pais):
        self.__pais=pais
    def set_id(self,id):
        self.__id=id
    
    def ingreso_registros(self):
        
        #REGISTRO DE NOMBRE
        valido=False
        while not valido:
            self.__nombre=input("Ingrese nombre y apellido:\n ")
            valido=check.check_name(self.__nombre)
            if not valido:
                print ("El ingreso no es correcto  ")
        
        #REGISTRO EMAIL
        valido=False   
        while not valido: 
            self.__email= input("Ingrese  email:\n  ")
            valido=check.check_email(self.__email)
            if not valido:
                print("El email ingresado no corresponde con el formato de email")
            else:
                valido=False
                query="select user_id from usuarios where email=%s"
                val=(self.__email,)
                db_ecommerce.get_cursor().execute(query, val)
                result=db_ecommerce.get_cursor().fetchone()
                if result is not None:
                    print("El mail ingresado ya se encuentra registrado, intente con otro email")
                else:
                    valido=True
        
        #REGISTRO PASSWORD
        valido=False
        while not valido:
            self.__password=getpass.getpass("Ingrese una contraseña :\n" )
            #self.__password=input("Ingrese una contraseña :\n" )
            valido=check.check_password(self.__password)
            if not valido:
                print("La contraseña debe contener al menos 8 caracteres, una letra mayuscula, una minuscula, un digito y algunos de los siguientes caracteres (?=.*?[#?!@$%^&*-]) \n ")
            else:
                valido=False
                self.__ver_password=getpass.getpass("Ingrese nuevamente la contraseña :\n" )
                #ver_password=input("Ingrese nuevamente la contraseña :\n" )
                if self.__password==self.__ver_password:
                   self.__password=base64.encodebytes(bytes(self.__password,"utf-8")).decode("utf-8")[:-1]
                   valido=True
                else:
                    print("Las contraseñas no coinciden")
    
    #REGISTRO CIUDAD    
    def ubicacion(self):
        print("Ingrese su ubicación actual")
        self.__pais=city.select_pais()
        self.__provincia=city.select_provincia()
        self.__ciudad=city.select_ciudad() 


    def registro(self):
        query="insert into usuarios(nombre, email, contrasenia, id_ciudad, id_provincia, id_pais ) values(%s,%s,%s,%s, %s,%s)"
        val=(self.get_nombre(), self.get_email(), self.get_password(),self.get_ciudad(),self.get_provincia(), self.get_pais())
        db_ecommerce.get_cursor().execute(query, val)
        db_ecommerce.conexion.commit()
        self.set_id(db_ecommerce.get_cursor().lastrowid)
        print("El registro se  ha completado exitosamente")
        input("Presione enter para continuar...")       
    
registro=New_User()
#user1=Usuario("pepe", 23564, 1111111, "peper@", "cuba1000")
#rint(user1.get_nro_tarjeta())
#registro.ubicacion()
