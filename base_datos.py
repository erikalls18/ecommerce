import mysql.connector
dbconf={
  'host':'localhost', 
  'user':'kafka',
  'password':'abcd1234',
  'database':'ecommerce' 
}

class Db_Ecommerce():
    def __init__(self):
        self.conexion=mysql.connector.Connect(**dbconf)
        self.cursor=self.conexion.cursor()

    def get_cursor(self):
        return self.cursor
    def get_conexion(self):
        return self.conexion

db_ecommerce=Db_Ecommerce()