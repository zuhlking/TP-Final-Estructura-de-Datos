class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo, leido = False):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._leido = leido

    def marcar_leido(self):
        self._leido = True

    def __str__(self):
        return f"De: {self.remitente}, Para: {self.destinatario}, Mensaje: {self.cuerpo}"