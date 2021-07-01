from registro import registro
from menu_compras import verOpciones
from carritto import carrito
from login import user
from opciones_user import user_options
import os

while True:
    os.system('cls')
    print("Bienvenido al gran e-commerce!!!!")
    print("1 - Registro de usuario")
    print("2 - Login de usuario")
    print("3 - Opciones de usuario")
    print("4 - Busqueda")
    print("5 - Carrito de compras")
    print("6 - Cerrar sesión")
    print("7 - Salir")
    valido=False
    while not valido:
        try:
            opcion=int(input("Ingrese la opcion deseada: "))
        except:
            print("Por favor, ingrese solo numeros!")
        else:
            if opcion>0 and opcion<=7:
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
        if user.get_email()=="":
            print("Para ver estas opciones  debes estar logueado")
            input("Presione enter para continuar...")
        else:
            user_options.seleccionar_opcion()
            if user_options.get_seleccion()==1:
               user_options.modificar_password()
            else:
                user_options.eliminar_cuenta()
    elif opcion==4:
         verOpciones.mostar_MenuCompras()
    elif opcion==5:
        carrito.ver_carrito()
        if len(carrito.get_chango()) > 0:
            carrito.eliminar_carrito()
            carrito.comprar()
    elif opcion==6:
        if user.get_email()=="":
            print("Para cerrar sesion debes estar logueado")
            input("Presione enter para continuar...")
        else: 
           user.logout()
             
    else:
        break
