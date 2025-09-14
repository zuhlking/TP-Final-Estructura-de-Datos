class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):
        self._mensajes.remove(mensaje)

    def listar_mensajes(self):
        return self._mensajes