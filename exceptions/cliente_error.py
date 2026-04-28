class ClienteError(Exception):
    def __init__ (self, mensaje, dato_invalido=None):
        super().__init__(mensaje)
        self.dato_invalido = dato_invalido
    def __str__(self):
        if self.dato_invalido is not None:
            return f"[ClienteError] {self.args[0]} -> Dato: {self.dato_invalido}"
        return f"[ClienteError] {self.args[0]}"
class EmailInvalidoError (ClienteError):
    def __str__(self):
        if self.dato_invalido is not None:
            return f"[EmailInvalidoError] {self.args[0]} -> Email: {self.dato_invalido}"
        return f"[EmailInvalidoError] {self.args[0]}"
class IdentificacionInvalidaError (ClienteError):
    def __str__(self):
        if self.dato_invalido is not None:
            return f"[IdentificacionInvalidaError] {self.args[0]} -> ID: {self.dato_invalido}"
        return f"[IdentificacionInvalidaError] {self.args[0]}"           