# ecommerce

Para ejecutar este programa, se hace desde el modulo menu.py. donde se despliegan las opciones
En la opción de registro el usurio ingresa su datos los cuales se registran en la base datos. El ingreso de la contraseña no es visible por la función getpass,en dado caso de querer visulizarla se comenta esta linea y se descomenta la siguiente. Siempre aparecerá de esta manera cuando se solicite su ingreso
En la opción de login  se inicia sesión.
En opciones de usuario, se puede modificar la contraseña o eliminar la cuenta
En busqueda, el usurio se encontrará con un submenú donde se muestran todos  los productos  y de acuerdo a su marca o categoría. Desde estas opciones  se peuden añadir productos  al carrito
En carritos de compras se puede eliminar productos o efectuar la compra.
En cerrar sesión se finaliza la sesión

Recuerde instalar los requerimientos que estan en el requirements.txt con:
pip install -r requirements.txt

Tambien debe importar la base de datos que se encuentra en el archivo base_de_datos.sql

Recuerde crear la base de datos "ecommerce" antes de importar el archivo base_de_datos.sql!