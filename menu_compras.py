from productos import producto
from categorias import cat
from marcas import mark
import os
class MenuCompras():
    def mostar_MenuCompras(self):
        while True:
            os.system('cls')
            print("Seleccione una opcion")
            print("1. Ver Categorias")
            print("2. Ver Marcas")
            print("3. Ver todo")
            print("4. Volver al menu principal")
            valido=False
            while not valido:
                try:
                    opcion=int(input("Ingrese la opcion deseada: "))
                except:
                    print("Seleccione una opcion valida! ")
                if opcion>=1 or opcion<=4:
                   valido=True
                
            if opcion==1:
                cat.mostrar_categorias()
                cat.seleccionar_categoria()
                cat.añadir_carrito()
            elif opcion==2:
                mark.mostrar_marcas()
                mark.seleccionar_marca()
                mark.añadir_carrito()
            elif opcion==3:
                producto.imprimir_producto()
                producto.añadir_carrito()
                
            elif opcion==4:
                break
            else:
                print("Seleccione una opción valida!!")
                input("Presione enter para continuar")
        
verOpciones=MenuCompras()