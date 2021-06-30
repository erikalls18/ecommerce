from registro import registro
from menu_compras import verOpciones
from carritto import carrito
from login import user
import os

while True:
    os.system('cls')
    print("Bienvenido al gran e-commerce!!!!")
    print("1 - Registro de usuario")
    print("2 - Login de usuario")
    print("3 - Busqueda")
    print("4 - Carrito de compras")
    print("5 - Cerrar sesión")
    print("6 - Salir")
    valido=False
    while not valido:
        try:
            opcion=int(input("Ingrese la opcion deseada: "))
        except:
            print("Por favor, ingrese solo numeros!")
        else:
            if opcion>0 and opcion<=6:
                valido=True
            else:
                print("La opcion esta fuera del rango!!!")

    if opcion==1:
        registro.ingreso_registros()
        registro.ubicacion()
        registro.registro()    
    elif opcion==2:
        user.login()
    elif opcion==3:
         verOpciones.mostar_MenuCompras()
    elif opcion==4:
        carrito.ver_carrito()
        if len(carrito.get_chango()) > 0:
            carrito.eliminar_carrito()
            carrito.comprar()
    elif opcion==5:
        if user.get_email()=="":
            print("Para cerrar sesion debes estar logueado")
            input("Presione enter para continuar")
        else: 
           user.logout()
             
    else:
        break
