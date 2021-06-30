from base_datos import db_ecommerce
from validate_email import validate_email
import base64
import re

class Validador():
    def __init__(self):
        pass

    def check_name(self, nombre):
        regex= "^([a-zA-Z]{2,10})([a-zA-Z ]{2,27})$"
        if re.match(regex, nombre) is None:
            return False
        else:
            return True
    def check_email(self, email):
       return validate_email(email)

    def check_password(self, password):
        regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if re.match(regex,password) is None:
            return False
        else:
            return True
    def check_ciudad(self,ciudad):
        pass


check=Validador()