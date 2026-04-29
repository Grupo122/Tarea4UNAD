# Módulo de excepciones personalizadas para el Cliente
# Se usa para manejar errores cuando los datos del cliente no son válidos

class ClienteError(Exception):
    """Error general del cliente."""

    def __init__(self, mensaje, dato_invalido=None):
        # Guarda el mensaje en la clase madre Exception
        super().__init__(mensaje)
        # Guarda el dato que causó el error
        self.dato_invalido = dato_invalido

    def __str__(self):
        # Si hay un dato inválido, lo muestra junto al mensaje
        if self.dato_invalido is not None:
            return f"[ClienteError] {self.args[0]} -> Dato: {self.dato_invalido}"
        # Si no hay dato inválido, solo muestra el mensaje
        return f"[ClienteError] {self.args[0]}"


class EmailInvalidoError(ClienteError):
    """Error cuando el email no tiene formato válido."""

    def __str__(self):
        # Si hay un email inválido, lo muestra junto al mensaje
        if self.dato_invalido is not None:
            return f"[EmailInvalidoError] {self.args[0]} -> Email: {self.dato_invalido}"
        # Si no hay email, solo muestra el mensaje
        return f"[EmailInvalidoError] {self.args[0]}"


class IdentificacionInvalidaError(ClienteError):
    """Error cuando la identificación está vacía o no es numérica."""

    def __str__(self):
        # Si hay una ID inválida, la muestra junto al mensaje
        if self.dato_invalido is not None:
            return f"[IdentificacionInvalidaError] {self.args[0]} -> ID: {self.dato_invalido}"
        # Si no hay ID, solo muestra el mensaje
        return f"[IdentificacionInvalidaError] {self.args[0]}"        