from base_datos import db_ecommerce
from carritto import carrito
from code import codes
import os

class Productos():
    def __init__(self):
       self.__codigo="" 
       self.__nombre=""
       self.__precio=""
       self.resultado=[]

    def get_codigo(self):
        return self.__codigo 
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio 
    def get_resultado(self):
        return self.resultado  
    def set_codigo(self, codigo):
        self.__codigo=codigo   
    def set_nombre(self, nombre):
        self.__nombre=nombre   
    def set_precio(self, precio):
        self.__precio=precio  
    def set_resultado(self,resultado):
        self.__resultado=resultado

    def imprimir_producto(self):
        os.system('cls')
        query="Select codigo,nombre, precio from productos"
        db_ecommerce.get_cursor().execute(query)
        self.__resultado=db_ecommerce.get_cursor().fetchall()
        codes.listar(self.__resultado)
        
      
    def añadir_carrito(self):
        valido=False
        while not valido:
            respuesta=str(input("¿Desea añadir un producto del carrito: Si/No ?  \n "))           
            if respuesta.lower()=="si" or respuesta.lower()=="no":    
                valido=True  
                if respuesta=="si":
                    carrito.agregar_carrito(self.__resultado)
                else:
                    break    
            else:
                print("Opción no valida")         
                    
    
            

producto=Productos()
#producto.imprimir_producto()
#producto.añadir_carrito()
#producto.mostar_menuProd()




   
        
            
            
     