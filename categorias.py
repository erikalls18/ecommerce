from carritto import carrito
from base_datos import db_ecommerce
from code import codes
import os

class Categorias():
    def __init__(self):
        self.__nombre=""
        self.__resultado=[]
        self.__id_categoria=[]
             
    def get_nombre(self):
        return self.__nombre
    def get_id_categoria(self):
        return self.__id_categoria
    def get_resultado(self):
        return self.__resultado
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_id_categoria(self,id_categoria):
        self.__id_categoria=id_categoria  
    def set_nombre(self,resultado):
        self.seleccion=resultado
  
  
    def mostrar_categorias(self):
        os.system('cls')
        query="Select * from categoria"
        db_ecommerce.get_cursor().execute(query)
        result=db_ecommerce.get_cursor().fetchall()
        #print("Seleccione la categoría de acuerdo a su  índice numérico:")
        self.__id_categoria=codes.listar_categoria(result)
        
    def seleccionar_categoria(self):
        valido=False
        while not valido:
            try:
                seleccion=int(input("Ingrese  el código de la categoria a seleccionar: "))
            except:
                 print("Ingrese una opción valida")
            else:
                if seleccion>=1 and seleccion<=len(self.__id_categoria):
                    os.system('cls')
                    valido=True
                    new_seleccion=(seleccion-1)
                    query="Select codigo, nombre, precio from productos where id_categoria=%s"
                    val=(self.__id_categoria[new_seleccion],)
                    db_ecommerce.get_cursor().execute(query,val)
                    self.__resultado=db_ecommerce.get_cursor().fetchall()
                    codes.listar(self.__resultado)
                else:
                    print("Ingrese una opción valida")

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

cat=Categorias()
#cat.mostrar_categorias()
#cat.seleccionar_categoria()