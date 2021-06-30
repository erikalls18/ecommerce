from base_datos import db_ecommerce
import os
from code import codes
from login import user
class Carrito():
    def __init__(self):
        self.__chango=[]
        self.__cod_compras=0
    def get_chango(self):
        return self.__chango
    def get_cod_compras(self):
        return self.__cod_compras
    def set_cod_compras(self,cod_compras ):
        self.__cod_compras=cod_compras
    def set_chango(self, chango):
        self.__chango=chango
        
    def agregar_carrito(self, resultado):   
        valido=False
        while not valido:
            try:
                print("Ingrese el codigo del producto a sumar al carrito o 0 para volver.")
                seleccion=int(input("Seleccione: "))
            except:
                print("Ingrese una opción valida")
            else:
                if seleccion==0:
                    break
                elif seleccion>=1 and seleccion <=len (resultado):
                    prod=resultado[seleccion-1]
                    self.__chango.append(prod)
                    print("El producto ha sido añadido al carrito")
                else:
                    print("El codigo ingresado no es valido")
                         
                print("Desea agregar mas productos al carrito Si/No: ")
                val=False
                while not val:
                    respuesta=str(input("Ingrese su respuesta: \n "))           
                    if respuesta.lower()=="si" or respuesta.lower()=="no":    
                        val=True 
                    else:
                        print("La opcion no es valida")        
                    if respuesta.lower()=="no":
                        valido=True
    
    def ver_carrito(self):
        if len(self.__chango) == 0:
            print("El carrito esta vacio!")
            input("Presione enter para continuar...")
        else:
            os.system("cls")
            print("Los productos añadidos a tu carrito son: ")
            codes.listar(self.__chango)
                         
    def eliminar_carrito(self):
    
        valido=False
        while not valido:
            if self.__chango==[]:
                break
            respuesta=str(input("¿Desea eliminar un producto del carrito: Si/No ?  \n "))           
            if respuesta.lower()=="si" or respuesta.lower()=="no":     
                if respuesta=="si":
                    val=False
                    while not val:
                        try:
                            respuesta1=int(input("Ingrese el indice del producto a eliminar:  \n "))    
                        except:
                            print("Seleccione una opción valida")
                        else:
                            if respuesta1>=1 and respuesta1 <=len(self.__chango):
                                val=True
                                res=(respuesta1-1)
                                self.__chango.pop(res)
                                os.system("cls")
                                codes.listar(self.__chango)
                                print("El producto ha sido eliminado  del carrito")
                            else:
                                print("Opción no valida")
            
                else:
                    valido=True
                        
    def comprar(self):
        valido=False
        while not valido:
            if self.__chango==[]:
                print("El carrito ha sido vaciado")
                input("Presione enter para continuar...")
                break
            respuesta=str(input("¿Desea relizar la compra Si/No:  "))          
            if respuesta.lower()=="si" or respuesta.lower()=="no": 
                valido=True   
                if respuesta=="si":
                    if user.get_email()=="":
                        print("Para realizar la compra debe estar logueado ")
                        input("Presione enter para continuar...")
                    else:
                        list_precio=[]
                        for i in self.__chango:
                            codigo,nombre, precio=i
                            query="Insert into  compras (id_user,nombre_user, email_user, id_producto, nombre_producto, precio)values(%s,%s,%s,%s,%s,%s)"
                            val=(user.get_id(), user.get_nombre(),user. get_email(),codigo,nombre, precio)
                            db_ecommerce.get_cursor().execute(query,val)
                            db_ecommerce.conexion.commit()
                            list_precio.append(precio)
                        total=sum(list_precio)
                        print(f"El total de tu compra es {total}")
                        print("Felicitaciones, tu compra se ha efectuado con éxito!") 
                        self.__chango=[]                          
                        input("Presione enter para continuar")                           
                else:
                    break
                        


carrito=Carrito()
#carrito.comprar()
#carrito.agregar_carrito()
#carrito.eliminar_carrito()
