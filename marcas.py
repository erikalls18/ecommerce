from base_datos import db_ecommerce
from carritto import carrito
from code import codes
import os

class Marca():
    def __init__(self, ):
        self.__nombre=""
        self.__id_marca=""
        self.__resultado=[]    
    
    def get_nombre(self):
        return self.__nombre
    def get_id_marca(self):
        return self.__id_marca
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_id_marca(self,marca):
        self.__id_marca=marca
    def set_resultado(self,resultado):
        self.__resultado=resultado
    
    def mostrar_marcas(self):
        os.system('cls')
        query="Select* from marca"
        db_ecommerce.get_cursor().execute(query)
        result=db_ecommerce.get_cursor().fetchall()
        self.__id_marca=codes.listar_marcas(result)
    
    def seleccionar_marca(self):
        valido=False
        while not valido:
            try:
                seleccion=int(input("Ingrese  el código de la marca a seleccionar: "))
            except:
                 print("Ingrese una opción valida")
            else:
                if seleccion>=1 and seleccion<=len(self.__id_marca):
                    os.system('cls')
                    valido=True
                    new_seleccion=(seleccion-1)
                    query="Select codigo, nombre,  precio from productos where id_marca=%s"
                    val=(self.__id_marca[new_seleccion],)
                    db_ecommerce.get_cursor().execute(query,val)
                    self.__resultado=db_ecommerce.get_cursor().fetchall()
                    codes.listar(self.__resultado)

    def añadir_carrito(self):  
                    valido=False
                    while  not valido:
                        respuesta=str(input("¿Desea añadir un producto del carrito: Si/No ?  \n "))           
                        if respuesta.lower()=="si" or respuesta.lower()=="no":    
                            valido=True  
                            if respuesta=="si":
                                carrito.agregar_carrito(self.__resultado) 
                            else:
                                break
                        else:
                            print("Selecciona una opción valida")

mark=Marca()
#mark.mostrar_marcas()
#mark.seleccionar_marca()