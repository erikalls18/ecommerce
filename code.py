from tabulate import tabulate
class Codes():
    def __init__(self):
        pass

    def listar(self, lista):
        listado = []
        j = 1
        for i in lista:
           producto = []
           id, nombre, precio=i
           producto.append(str(j))
           #producto.append(codigo)
           producto.append(nombre)
           producto.append(precio)
           listado.append(producto)
           j = j + 1 
        print(tabulate(listado, headers=['Codigo','Producto','Precio']))
    
    def listar_categoria(self, listado):
        cat_listado=[]
        cat_id=[]
        j=1
        for i in listado:
            
            cat_name = []  
            cat_name.append(str(j))
            cat_name.append(i[1])
            cat_id.append(i[0])
            cat_listado.append(cat_name)
            j=j+1
        list_id_categoria=cat_id
        print(tabulate(cat_listado, headers=['Codigo','Categoria']))
        return list_id_categoria

    def listar_marcas(self, listado):
        marcas_listado=[]
        marca_id=[]
        j=1
        for i in listado:
            marca_name = []  
            marca_name.append(str(j))
            marca_name.append(i[1])
            marca_id.append(i[0])
            marcas_listado.append(marca_name)
            j=j+1
        list_id_marca=marca_id
        print(tabulate(marcas_listado, headers=['Codigo','Marca']))
        return list_id_marca

codes=Codes()