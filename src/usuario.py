from carpeta import Carpeta
class Usuario:
    def __init__(self, id, nombre, email, password):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.carpetas = {"Inbox": Carpeta("Inbox"), "Enviados": Carpeta("Enviados"), "Spam": Carpeta("Spam")}

    def verificar_password(self, password):
        return self.password == password
    
    def recibir_mensaje(self, mensaje):
        pass
    
    def enviar_mensaje(self, destinatario, asunto, cuerpo, servidor):
        pass   
    
    def crear_carpeta(self, nombre):
        pass
    
    def listar_carpetas(self):
        return list(self.carpetas.keys())
        
 