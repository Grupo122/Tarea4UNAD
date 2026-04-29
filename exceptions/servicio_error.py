# Módulo de excepciones personalizadas para los Servicios
# Se usa para manejar errores cuando hay problemas con los servicios del sistema

class ServicioError(Exception):
    """Error general de los servicios del sistema."""

    def __init__(self, mensaje, servicio=None):
        # Guarda el mensaje en la clase madre Exception
        super().__init__(mensaje)
        # Guarda el nombre del servicio que causó el error
        self.servicio = servicio

    def __str__(self):
        # Si hay un servicio, lo muestra junto al mensaje
        if self.servicio is not None:
            return f"[ServicioError] {self.args[0]} -> Servicio: {self.servicio}"
        # Si no hay servicio, solo muestra el mensaje
        return f"[ServicioError] {self.args[0]}"


class ServicioNoDisponibleError(ServicioError):
    """Error cuando el servicio solicitado no está disponible."""

    def __str__(self):
        # Si hay un servicio, lo muestra junto al mensaje
        if self.servicio is not None:
            return f"[ServicioNoDisponibleError] {self.args[0]} -> Servicio: {self.servicio}"
        # Si no hay servicio, solo muestra el mensaje
        return f"[ServicioNoDisponibleError] {self.args[0]}"


class ParametroInvalidoError(ServicioError):
    """Error cuando un parámetro enviado al servicio no es válido."""

    def __str__(self):
        # Si hay un servicio, lo muestra junto al mensaje
        if self.servicio is not None:
            return f"[ParametroInvalidoError] {self.args[0]} -> Servicio: {self.servicio}"
        # Si no hay servicio, solo muestra el mensaje
        return f"[ParametroInvalidoError] {self.args[0]}"


class CostoInvalidoError(ServicioError):
    """Error cuando el costo calculado es negativo o no válido."""

    def __str__(self):
        # Si hay un servicio, lo muestra junto al mensaje
        if self.servicio is not None:
            return f"[CostoInvalidoError] {self.args[0]} -> Servicio: {self.servicio}"
        # Si no hay servicio, solo muestra el mensaje
        return f"[CostoInvalidoError] {self.args[0]}"