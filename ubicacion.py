
from base_datos import db_ecommerce
class Ciudad():
    def __init__(self):
        self.__Paises=[]
        self.__Provincias=[]
        self.__ciudades=[]
        self.__cod_ciudad=""
        self.__cod_Provincia=""
        self.__cod_Pais=""

    def get_paises(self):
        return self.__Paises
    def get_provincias(self):
        return self.__Provincias
    def get_ciudades(self):
        return self.__ciudades
    def get_cod_Pais(self):
        return self.__cod_Pais
    def get_cod_provincia(self):
        return self.__cod_Provincia
    def get_cod_ciudad(self):
        return self.__cod_ciudad
    
    def set_pais(self,paises):
        self.__Paises=paises
    def set_provincia(self,provincia):
        self.__Provincias=provincia
    def set_ciudad(self,ciudad):
        self.__ciudades=ciudad


    def select_pais(self):
        query="Select pais_id, nombre from pais"
        db_ecommerce.get_cursor().execute(query)
        self.__Paises= db_ecommerce.get_cursor().fetchall()
        print("Seleccione el país según el índice numérico:")
        for i, pais in enumerate(self.__Paises):
            print(i+1, pais[1])
        valido=False
        while not valido:
            try:
                seleccion=int (input("Seleccione: "))                   
            except:
                print("Seleccione una opcion valida")
            else:
                if seleccion >=1 and seleccion <= len(self.__Paises):
                    valido=True 
                    pais=self.__Paises[seleccion-1]
                    self.__cod_Pais=pais[0]
                else:
                  print ("El ingreso no es valido, intente nuevamente")
        return self.__cod_Pais
    
    def select_provincia(self):
        query="Select provincia_id, nombre from provincia where id_pais=%s"
        val=(self.__cod_Pais,)
        db_ecommerce.get_cursor().execute(query,val)
        self.__Provincias= db_ecommerce.get_cursor().fetchall()
        print("Seleccione la provincia según el índice numérico:")
        for i, provincia in enumerate(self.__Provincias):
            print(i+1, provincia[1])
        valido=False
        while not valido:
            try:
                seleccion=int (input("Seleccione: "))
            except:
                print("Seleccione una opción valida")
            else:
                if seleccion >=1 and seleccion <= len(self.__Provincias):
                    valido=True 
                    provincia=self.__Provincias[seleccion-1]
                    self.__cod_Provincia=provincia[0]
                   
                else:
                  print ("El ingreso no es valido, intente nuevamente")
        return self.__cod_Provincia
    
    
    def select_ciudad(self): 
        query="Select ciudad_id, nombre from ciudad where id_provincia=%s"
        val=(self.__cod_Provincia,)
        db_ecommerce.get_cursor().execute(query,val)
        self.__ciudades = db_ecommerce.get_cursor().fetchall()
        print("Seleccione la ciudad según el índice numérico:")
        for i, ciudad in enumerate(self.__ciudades):
           print(i+1, ciudad[1]) 
        valido=False
        while not valido:
            try:
                seleccion=int (input("Seleccione: ")) 
            except:
                print("Seleccione una opcion valida")
            else:
                if seleccion >=1 and seleccion <=len(self.__ciudades):
                  valido=True 
                  ciudad=self.__ciudades[seleccion-1]
                  self.__cod_ciudad=ciudad[0]
               
                else:
                  print ("El ingreso no es valido, intente nuevamente")
        return self.__cod_ciudad
        
city=Ciudad()
#city.get_pais()
#city.get_provincia()
#city.get_ciudad()