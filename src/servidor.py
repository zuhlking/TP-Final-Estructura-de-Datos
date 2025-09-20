from usuario import Usuario
from mensaje import Mensaje

class ServidorCorreo:
    def __init__(self):
        self._usuarios = {}

    def registrar_usuario(self, id_usuario, nombre, email, password):
        if email not in self._usuarios:
            usuario = Usuario(id_usuario, nombre, email, password)
            self._usuarios[email] = usuario
            return usuario
        else:
            print("El email ya está registrado")
            return None

    def autenticar_usuario(self, email, password):
        usuario = self._usuarios.get(email)
        if usuario and usuario.verificar_password(password):
            return usuario
        return None

    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        if remitente.email in self._usuarios and destinatario.email in self._usuarios:
            mensaje = Mensaje(remitente.email, destinatario.email, asunto, cuerpo)
            # Nota para recordar, agrega al inbox del destinatario
            destinatario.carpetas["Inbox"].agregar_mensaje(mensaje)
            # Nota para recordad, agrega a enviados del remitente
            remitente.carpetas["Enviados"].agregar_mensaje(mensaje)
            return mensaje
        else:
            print("Error: remitente o destinatario no registrados")
            return None

    def listar_usuarios(self):
        return list(self._usuarios.keys())